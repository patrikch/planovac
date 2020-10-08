import sqlite3

db = "D:\\zz Nove Jazyky\\Python\\PlanovacApp\\Planovac\\db\\db.sqlite3"

class Database:    
    def __init__(self,dbFile=None):
        if not dbFile:
            self._dbFile = db
        else:
            self._dbFile = dbFile

    def get_one_record(self,sql,filters):
        cnn = sqlite3.connect(self._dbFile)
        c = self._execute_get_cursor(cnn,sql,filters)
        row = c.fetchone()
        cnn.close()
        return dict(zip([column[0] for column in c.description], row))

    def get_records(self,sql,filters):
        cnn = sqlite3.connect(self._dbFile)
        c = self._execute_get_cursor(cnn,sql,filters)
        rows = c.fetchall()
        cnn.close()
        return [dict(zip([column[0] for column in c.description], row)) for row in rows]

    def run(self,sql,values):
        cnn = sqlite3.connect(self._dbFile)
        c = cnn.cursor()
        c.execute(sql,values)
        cnn.commit()
        cnn.close()    

    def _execute_get_cursor(self,cnn,sql,filters):
        c = cnn.cursor()
        if len(filters) > 0:
            c.execute(sql,filters)
        else:
            c.execute(sql)
        return c

if __name__ == "__main__":
    db = Database("D:\\zz Nove Jazyky\\Python\\PlanovacApp\\db\\db.sqlite3")
    recs = db.get_records("select * from [User] where name like ?",["V%",])
    print("test records" + "\n")
    print(str(len(recs)))
    print(str(recs[0]))
    rec = db.get_one_record("select * from [User] where id=?",[1,])
    print("test one record" + "\n")
    print(str(rec))
    print("test insert" + "\n")
    db.run("INSERT INTO user(name,surname,username,password) VALUES(?,?,?,?)" \
           ,["Roman","Studený","romans","abcdef1."])
    recs = db.get_records("select * from user",[])
    print(str(recs[len(recs)-1]))
    print("done")
    
        
    
        
