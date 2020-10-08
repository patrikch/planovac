import xml.etree.ElementTree as etree
from datetime import datetime
from core.project import Project,Job,Engine
import os

class ProjectFile:
    def __init__(self):
        pass

    def _putProject2Dict(self,proj):
        return {"owner":proj.owner,
                 "dt_from":proj.dtFrom,
                 "dt_to":proj.dtTo,           
                 }        

    def _putEngine2Dict(self,eng):        
        return {"name":eng.name,}

    def _putJob2Dict(self,job):
        return {"name":job.name,
                "days":str(job.days),
                "duration":str(job.duration),
                "start":job.start,
                "color":job.color,
                }
        
    def save(self,file,project):
        root = etree.Element("root")
        d = self._putProject2Dict(project)
        pElem = etree.SubElement(root,"project",d)
        for eng in project.engines:
            d = self._putEngine2Dict(eng)
            eElem = etree.SubElement(pElem,"engine",d)
            jobs = [j for j in project.jobs if j.engine == eng.name]
            for job in jobs:
                d = self._putJob2Dict(job)
                jElem = etree.SubElement(eElem,"job",d)
                
        tree = etree.ElementTree(root)
        tree.write(file, xml_declaration=True, encoding='utf-8')

    def read(self,file,owner):
        _, tail = os.path.split(file)
        p = Project(None)
        tree = etree.parse(file)
        root = tree.getroot() #tj.root
        for child in root: #tj.project
            p_att = child.attrib
            #p.file = file
            p.name = tail
            p.owner = owner #p_att["owner"]
            p.dtFrom = datetime.strptime(p_att["dt_from"], "%d.%m.%Y")
            p.dtTo = datetime.strptime(p_att["dt_to"], "%d.%m.%Y")
            p.folderId = None            
            for subChild in child: #tj.engine
                e = Engine(None)
                e_att = subChild.attrib
                e.name = e_att["name"]
                for subSubChild in subChild: #tj.job
                    j = Job(None)
                    j_att = subSubChild.attrib
                    j.name = j_att["name"]
                    j.days = int(j_att["days"])
                    j.duration = int(j_att["duration"])
                    j.start = datetime.strptime(j_att["start"], "%d.%m.%Y")
                    j.color = j_att["color"]
                    #j.engine = e.name
                    e.addJob(j)
                p.addEngine(e)
        return p

if __name__ == "__main__":
    p_file = ProjectFile()
    file1 = "D:\\myData\\Projekty II\\PlanovacApp4\\PlanovacApp\\bin\\" + \
            "Debug\\data\\testCopyPaste3.pln"
    file2 = "D:\\zz Nove Jazyky\\Python\\PlanovacApp\\Planovac\\core\\files\\2015-2016.pln"
    proj = p_file.read(file2)
    print(len(proj.engines))
    jobs = 0
    for eng in proj.engines:
        jobs += len(eng)
            
    print(len(jobs))
    
    #file = "D:\\myData\\Projekty II\\PlanovacApp4\\PlanovacApp\\bin\\" + \
    #                   "Debug\\data\\testCopyPaste3.pln"
    #p_file.save(file,proj)
    print("done")
                
        
    
