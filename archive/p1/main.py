from datetime import datetime
from core.user import User
from core.project import Project,Engine,Job
from core.dateRange import DateRange
from db.sqliteDatabase import Database 
from core.projectFile import ProjectFile

def printTree(tree):
    for n in tree:
        print(str(n))
        for sn in n.children:
            print("\t" + str(sn))
            for ssn in sn.children:
                print("\t\t" + str(ssn))
                for sssn in ssn.children:
                    print("\t\t\t" + str(sssn))

def printProj(p):
    print(str(p))
    for e in p.engines:
        print("\t" + str(e))
        for j in e.jobs:
            print("\t\t" + str(j))
            
        
def user_test(wholeTree=True):
    patrik = User()
    patrik.login("patrikch","123456")
    print(patrik.is_logged)
    print(str(patrik))
    tree = patrik.project_tree
    printTree(tree)
    #p = Project(1)
    #p.fill(wholeTree)
    #printProj(p)

def range_test():
    dtFrom = datetime.strptime("2015-09-01", "%Y-%m-%d")
    dtTo = datetime.strptime("2015-12-31", "%Y-%m-%d")
    rozsah = DateRange(dtFrom,dtTo)
    lst = rozsah.get_range_days()
    print("nalezeno dni:" + str(len(lst)))
    for d in lst:
        print(str(d))

def job_enddate_test():
    sql = "select * from job where id=?"
    row = Database().get_one_record(sql,[3,])
    job = Job(row)
    print(job)
    print("end=" + str(job.end))
    dtFrom = datetime.strptime("2015-01-01", "%Y-%m-%d")
    dtTo = datetime.strptime("2015-06-30", "%Y-%m-%d")
    rozsah = DateRange(dtFrom,dtTo)
    lst = rozsah.get_range_days()
    print("nalezeno dni:" + str(len(lst)))
    counter = 1
    for i,d in enumerate(lst):
        if d >= datetime.strptime("2015-01-14", "%Y-%m-%d"):
            print(str(counter) + " -> " + str(d))
            counter += 1

if __name__ == "__main__":
    #job_enddate_test()
    range_test()
    print("done")

    
