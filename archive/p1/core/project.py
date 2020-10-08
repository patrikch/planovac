from datetime import datetime

from db.sqliteDatabase import Database
from core.dateRange import DateRange

class Engine:
    def __init__(self,row):
        self.jobs = []
        self.id = -1
        self.name = ""
        self.project = None
        if row != None:
            self.id = int(row["id"])
            self.name = row["name"]
            self.project = int(row["projectId"])
        
    def addJob(self,job):
        self.jobs.append(job);

    def __len__(self):
        return len(self.jobs)

    def __getitem__(self,position):
        return self.jobs[position]

    def __repr__(self):
        return "Engine({0},jobs:{1})".format(self.name,str(len(self.jobs)))
    
class Job:
    def __init__(self,row):
        self.id = -1
        self.name = ""
        self.duration = None
        self.days = None
        self.start = None        
        self.color = None
        self.engine = None
        self.row = 0
        if row != None:
            self.id = int(row["id"])
            self.name = row["name"]
            self.duration = int(row["duration"])
            self.days = int(row["days"])
            self.start = datetime.strptime(row["start"], "%Y-%m-%d")
            self.color = row["color"]
            self.engine = int(row["engineId"])

    @property
    def end(self):
       row = self.get_job_project()
       dtFrom = datetime.strptime(row["dtFrom"], "%Y-%m-%d")
       dtTo = datetime.strptime(row["dtTo"], "%Y-%m-%d")
       dr = DateRange(dtFrom,dtTo)
       end = dr.get_day(self.start,self.days)           
       return end

    def get_job_project(self):
        sql = "select project.* from engine inner join project on engine.projectId=" \
              "project.id where engine.id=?"
        row = Database().get_one_record(sql,[self.engine,])
        return row        

    def __repr__(self):
        return "Job({0} - {1},eng:{2})".format(str(self.id),self.name,self.engine)
    
class Project:
    def __init__(self,id=None):
        self.id = -1
        if id:
           self.id = id         
        self.name = ""
        self.owner = None
        self.dtFrom = None
        self.dtTo = None        
        self.engines = []
        self.folder = None
        self.folderId = 0        
                
    def fill(self,wholeTree=True):
        if self.id == -1:
            raise Exception("Correct project.id is not set.")

        sql = "select * from project where id=?"
        row = Database().get_one_record(sql,[self.id,])
        if row != None:
            #self.id = int(row["id"])
            self.name = row["name"]
            self.owner = int(row["ownerId"])
            self.dtFrom = datetime.strptime(row["dtFrom"], "%Y-%m-%d")
            self.dtTo = datetime.strptime(row["dtTo"], "%Y-%m-%d")
            if row["folderId"] != None:
                self.folderId = int(row["folderId"])

            if wholeTree:
                sql = "select * from engine where projectId=?"
                engines = Database().get_records(sql,[self.id,])
                sql = "select job.* from job inner join engine on " + \
                      " job.engineId = engine.id where  engine.projectId = ?"
                jobs = Database().get_records(sql,[self.id,])
                for r in engines:
                    e = Engine(r)
                    eJobs = [j for j in jobs if int(j["engineId"]) == e.id]
                    for job in eJobs:
                        e.addJob(Job(job))
                    self.addEngine(e)                    
    
    def addEngine(self,eng):
        self.engines.append(eng)                

    def __repr__(self):
        #_,filename = os.path.split(self.file)
        return "Project({0},{1}-{2},eng:{3})".format(self.name,str(self.dtFrom),
                                                              str(self.dtTo),str(len(self.engines)))
class SharedProject:
    def __init__(self):
        self.project = None
        self.user = None
        self.role = None

    def __repr__(self):
        return "SharedProject({0} - {1} - {2})".format(str(self.project),str(self.user),str(self.role))
