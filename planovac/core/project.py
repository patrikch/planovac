from datetime import datetime
from planovacv2.core import daterange

class Engine:
    def __init__(self):
        self.jobs = []
        self.id = -1
        self.name = ""
        self.project = None

    def assign_row(self):
        if len(self.jobs) == 0:
            return

        for j in self.jobs:
            j.row = 0

        row = 1
        prev_job = None
        while self._get_jobs_without_row()>0:
            #find lowest start - row first job
            min_job = self._find_first()
            min_job.row = row
            prev_job = min_job
            #find others
            self._find_others(prev_job,row)
            row += 1

    def sorted_jobs(self):
        self.assign_row()
        lst = sorted(j.row for j in self.jobs)
        rows = set(lst)
        sorted_jobs = []
        for r in rows:
            row_jobs = sorted([j for j in self.jobs if j.row == r],key = lambda x: x.start) 
            for j in row_jobs:
                sorted_jobs.append(j)
                
        return sorted_jobs

    def _find_others(self,prev_job,row):
        next_job = self._find_next(prev_job)
        while(next_job != None):
            next_job.row = row
            prev_job = next_job
            next_job = self._find_next(prev_job)

    def _find_next(self,prev_job):
        count = len([j for j in self.jobs if j.row == 0 and j.start > prev_job.end])
        if count == 0:
            return None
        else:
            min_diff = min((j.start-prev_job.end).days for j in self.jobs if j.row == 0 and j.start > prev_job.end)
            min_diff_job = [j for j in self.jobs if j.row == 0 and (j.start-prev_job.end).days == min_diff][0]
            return min_diff_job

    def _find_first(self):
        min_start = min(j.start for j in self.jobs if j.row == 0)
        min_job = [j for j in self.jobs if j.start == min_start][0]
        return min_job

    def _get_jobs_without_row(self):
        return len([j for j in self.jobs if j.row == 0])
        
    def add_job(self,job):
        self.jobs.append(job)

    def __len__(self):
        return len(self.jobs)

    def __getitem__(self,position):
        return self.jobs[position]

    def __repr__(self):
        return "Engine({0},jobs:{1})".format(self.name,str(len(self.jobs)))
    
class Job:
    def __init__(self):
        self.id = -1
        self.name = ""
        self.duration = None
        self.days = None
        self.start = None        
        self.color = None
        self.row = 0
        self.project = None

    @property
    def end(self):
       dr = daterange.DateRange(self.start,None)
       end = dr.get_day(self.start,self.days)           
       return end     

    def __repr__(self):
        return "Job({0} - {1})".format(str(self.id),self.name)
    
class Project:
    def __init__(self):
        self.id = -1        
        self.name = ""
        self.owner = None
        self.dtFrom = None
        self.dtTo = None        
        self.engines = []
        self.folder = None

    def __len__(self):
        return len(self.engines)
    
    def add_engine(self,eng):
        self.engines.append(eng)                

    def __repr__(self):
        #_,filename = os.path.split(self.file)
        return "Project({0},{1}-{2},eng:{3})".format(self.name,str(self.dtFrom),
                                                              str(self.dtTo),str(len(self.engines)))
