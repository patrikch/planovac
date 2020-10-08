import os.path
import sqlite3

class DbCreator:

    def __init__(self,folder_rel,file):
        folder_abs = os.path.abspath(folder_rel)
        self.path = os.path.join(folder_abs,file)
        
    def exists(self):
        return os.path.exists(self.path)

    def create(self):
        if self.exists():
            return False
        
        cnn = None
        try:
            cnn = sqlite3.connect(self.path)
            self._create_table(cnn,
                               """CREATE TABLE 'bank_holiday' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'day' DATETIME NOT NULL )"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'engine' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'name' VARCHAR NOT NULL , 'projectId' INTEGER NOT NULL )"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'folder' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'name' VARCHAR NOT NULL , 'parent' INTEGER,'userId' INTEGER NOT NULL)"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'predef_unit' ('id' INTEGER PRIMARY KEY  NOT NULL ,
                               'unit' VARCHAR NOT NULL ,'color' VARCHAR NOT NULL )"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'project' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'name' VARCHAR NOT NULL , 'ownerId' INTEGER NOT NULL, 'dtFrom' DATETIME NOT NULL ,
                               'dtTo' DATETIME NOT NULL , 'folderId' INTEGER)"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'role' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'name' VARCHAR NOT NULL , 'descr' VARCHAR)"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'shared_project' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'projectId' INTEGER NOT NULL , 'userId' INTEGER NOT NULL ,'roleId' INTEGER NOT NULL )"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'unit' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'name' VARCHAR NOT NULL , 'engineId' INTEGER NOT NULL , 'duration' INTEGER NOT NULL ,
                               'start' DATETIME NOT NULL , 'days' INTEGER NOT NULL , 'color' VARCHAR NOT NULL )"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'user' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , 'name' VARCHAR,
                               'surname' VARCHAR, 'password' VARCHAR, 'username' VARCHAR)"""
                               )
            self._create_table(cnn,
                               """CREATE TABLE 'worker_capacity' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,
                               'unit' VARCHAR NOT NULL , 'from_date' DATETIME , 'count' INTEGER NOT NULL )"""
                               )
            return True
        finally:
            if cnn != None:
                cnn.close()
                cnn = None
        
        
    def _create_table(self,cnn,sql):
        cnn.execute(sql)
        

if __name__ == "__main__":
    cr = DbCreator("../data","file.db")
    if not cr.exists():
        cr.create()
    #print("exists=" + str(exists))
    print("done")
