from db.sqliteDatabase import Database
from core.project import Project
from core.folderTree import FolderTree

class User:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.username = ""
        self.id = -1
        self.projects = []
        self.projectTree = None

    def login(self,username,password):        
        sql = "select * from user where username=? and password=?"
        row = Database().get_one_record(sql,[username,password])
        if row != None:
            self.id = int(row["id"])
            self.name = row["name"]
            self.surname = row["surname"]
            self.username = row["username"]
            self.projectTree = FolderTree(self.id)

    @property
    def is_logged(self):
        return self.id != -1

    @property
    def project_tree(self):        
        return self.projectTree.get_tree        
                
    def __len__(self):
        return len(self.projects)

    def __getitem__(self,position):
        return self.projects[position]

    def __repr__(self):
        return "User({0} - {1},{2})".format(str(self.id),self.name + " " + self.surname, \
                                            self.username)

class Role:
    def __init__(self):
        self.id = -1
        self.name = ""

    def __repr__(self):
        return "Role({0} - {1})".format(str(self.id),self.name)
    
class Folder:
    def __init__(self):
        self.id = -1
        self.name = ""
        self.parent = None
        self.user = None
        
    def __repr__(self):
        return "Folder({0} - {1},parent:{2})".format(self.name,str(self.id),str(self.parent))

