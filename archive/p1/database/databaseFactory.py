from db.sqliteDatabase import Database
import configparser


class DatabaseFactory:
    def get_db_object(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        debug_mode = int(config['DEFAULT']['debugMode'])
        if not debug_mode:
            return Database()
        else:
            return MockDatabase()

class MockDatabase:
    def __init__(self):
        self.row = None
        self.rows = None
        
    def set_one_row_result(self,row):
        self.row = row

    def set_many_rows_result(self,rows):
        self.rows = rows

    def get_one_record(self,sql,filters):
        return self.row

    def get_records(self,sql,filters):
        return self.rows

    def run(self,sql,values):
        pass

if __name__ == "__main__":
    db = DatabaseFactory().get_db_object()
    print(db.__class__)
    print("done")

    

    
        
        
        
