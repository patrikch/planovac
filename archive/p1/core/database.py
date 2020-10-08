import pyodbc

cnn_string = "DRIVER={SQL SERVER};SERVER=cztnspg-sq02;DATABASE=EON;UID=EonUser;PWD=x$83djYcHVZm"

class DatabaseLayer:
    def __init__(self,cnnString):
        self.cnn_string = cnnString

    def getOneRecord(self,sql,filters):        
        cnn = pyodbc.connect(self.cnn_string)
        cursor = cnn.cursor()
        if len(filters) > 0:
            cursor.execute(sql,filters)
        else:
            cursor.execute(sql)
        row = cursor.fetchone()
        cnn.close()
        return dict(zip([column[0] for column in cursor.description], row))
    
    def getRecords(self,sql,filters):
        cnn = pyodbc.connect(self.cnn_string)
        cursor = cnn.cursor()
        if len(filters) > 0:
            cursor.execute(sql,filters)
        else:
            cursor.execute(sql)
        rows = cursor.fetchall()
        cnn.close()
        return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

    def run(self,sql,values):
        cnn = pyodbc.connect(self.cnn_string)
        cursor = cnn.cursor()
        cursor.execute(sql,values)
        cnn.commit()
        cnn.close()

if __name__ == "__main__":
    db = DatabaseLayer(cnn_string)
    #recs = db.getRecords("select * from [User] where name like ?",["Dana%",])
    ##rec = db.getOneRecord("select * from [User] where id=?",[1,])
    #print(str(len(recs)))
    #print(str(recs[1]))
    db.run("INSERT INTO Pokus(den,mesic,rok) VALUES(?,?,?)",[3,6,2015])
    recs = db.getRecords("select * from Pokus",[])
    print(str(recs[len(recs)-1]))
    print("done")
