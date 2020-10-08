from datetime import datetime
from sqliteDatabase import Database

class DatabaseTable:
    def insert(self,tablename,values):
        """values is dictionary - key=column name,value=column value"""
        db = Database()
        template = "insert into {0}({1}) values({2})"
        t = self._get_insert_parameters(values)
        params = t[0]
        cols = t[1]
        question = self._get_questions(values)        
        sql = template.format(tablename,cols,question)
        db.run(sql,params)
    
    def insert_get_id(self,tablename,values):    
        self.insert(tablename,values)
        sql = "select max(id) as maxid from " + tablename        
        row = Database().get_one_record(sql,[])
        return int(row["maxid"])    
 
    def update(self,tablename,values,id):
        db = Database()
        template = "update {0} set {1} where id=?"
        t = self._get_update_parameters(values)
        params = t[0]
        params.append(id)
        cols = t[1]
        sql = template.format(tablename,cols)
        db.run(sql,params)

    def delete(self,tablename,id):
        db = Database()
        template = "delete from {0} where id=?"
        params = [id,]        
        sql = template.format(tablename)
        db.run(sql,params)

    def get(self,tablename,id):
        db = Database()
        template = "select * from {0} where id=?"
        params = [id,]        
        sql = template.format(tablename)
        row = db.get_one_record(sql,params)
        return row

    def select(self,tablename,values):
        db = Database()
        template = "select * from {0} where {1}"
        t = self._get_update_parameters(values," AND ")
        params = t[0]
        cols = t[1]
        sql = template.format(tablename,cols)
        rows = db.get_records(sql,params)
        return rows

    def _get_questions(self,values):
        question = ""
        for i in range(len(values)):
            if len(question) > 0:
                question += ","
            question += "?"
        return question
    
    def _get_insert_parameters(self,values):
        params = []
        cols = ""
        for k,v in values.items():
            if len(cols) > 0:
                cols += ","
            cols += k
            params.append(v)
        return (params,cols)

    def _get_update_parameters(self,values,spojka=","):
        params = []
        cols = ""
        for k,v in values.items():
            if len(cols) > 0:
                cols += spojka
            cols += k + "=?"
            params.append(v)
        return (params,cols)

if __name__ == "__main__":
    #d = {}
    #d["name"] = "pokus_1"
    #d["ownerId"] = 3
    #d["dtFrom"] = datetime.strptime("2015-09-03","%Y-%m-%d")
    #d["dtTo"] = datetime.strptime("2015-11-03","%Y-%m-%d")
    #d["folderId"] = 1
    p = DatabaseTable()
    #id = p.insert_get_id("project",d)
    #p.update("project",d,9)
    #print("updated")
    #print("projectId=" + str(id))
    #r = p.get("project",9)
    #print(str(r))
    p.delete("project",9)
    f = {}
    f["ownerId"] = 1
    rs = p.select("project",f)
    print(str(rs))
    print("done")
