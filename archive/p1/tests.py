import unittest
from datetime import datetime
from core.projectFile import ProjectFile
from core.user import User
from core.dateRange import DateRange
from db.databaseFactory import DatabaseFactory


class OldFileReader(unittest.TestCase):            

    owner = 2
    
    def test_tree_read_engine_count(self):
        """Project file should have 41 engines"""
        p_file = ProjectFile()
        file2 = "D:\\zz Nove Jazyky\\Python\\PlanovacApp\\Planovac\\core\\files\\2015-2016.pln"        
        proj = p_file.read(file2,self.owner)
        self.assertEqual(41,len(proj.engines))

    def test_tree_read_job_count(self):
        """Project file should have 229 jobs"""
        p_file = ProjectFile()
        file2 = "D:\\zz Nove Jazyky\\Python\\PlanovacApp\\Planovac\\core\\files\\2015-2016.pln"
        proj = p_file.read(file2,self.owner)
        jobs = 0
        for eng in proj.engines:
            jobs += len(eng)
        self.assertEqual(229,jobs)
        
class UserTesting(unittest.TestCase):

    def test_user_was_logged(self):
        """User should has been logged"""
        patrik = User()
        patrik.login("patrikch","123456")
        self.assertEqual(True,patrik.is_logged)

    def test_user_project_tree(self):
        """User folder-project tree should be different"""
        patrik = User()
        patrik.login("patrikch","123456")
        tree = patrik.project_tree
        self.assertEqual(1,len(tree))
        self.assertEqual("root",tree[0].name)
        self.assertEqual(4,len(tree[0].children))
        self.assertEqual("d",tree[0].children[0].type)
        self.assertEqual("d",tree[0].children[1].type)
        self.assertEqual("d",tree[0].children[2].type)
        self.assertEqual("p",tree[0].children[3].type)
        self.assertEqual(6,len(tree[0].children[0].children))
        self.assertEqual("d",tree[0].children[0].children[0].type)
        self.assertEqual("d",tree[0].children[0].children[1].type)
        self.assertEqual("p",tree[0].children[0].children[2].type)
        self.assertEqual("p",tree[0].children[0].children[3].type)
        self.assertEqual("p",tree[0].children[0].children[4].type)
        self.assertEqual("p",tree[0].children[0].children[5].type)        
        
class DatabaseFactoryTesting(unittest.TestCase):

    def test_mock_db_is_set(self):
        """Mock database should be set"""
        db = DatabaseFactory().get_db_object()        
        self.assertIn("MockDatabase",str(db.__class__))

class DateRangeTesting(unittest.TestCase):

    def test_get_range_days(self):
        """Between 1.10.2015 and 31.10.2015 should be 21 working days"""   
        dtFrom = datetime.strptime("2015-10-01", "%Y-%m-%d")
        dtTo = datetime.strptime("2015-10-31", "%Y-%m-%d")
        dtRange = DateRange(dtFrom,dtTo)
        svatek = datetime.strptime("2015-10-28", "%Y-%m-%d")
        dtRange.svatky = [svatek]
        days = dtRange.get_range_days()
        self.assertEqual(21,len(days))
        
    def test_kolikaty_right(self):
        """Between 1.10.2015 and 31.10.2015 9.10.2015 should be index=6"""   
        dtFrom = datetime.strptime("2015-10-01", "%Y-%m-%d")
        dtTo = datetime.strptime("2015-10-31", "%Y-%m-%d")
        dtRange = DateRange(dtFrom,dtTo)
        svatek = datetime.strptime("2015-10-28", "%Y-%m-%d")
        dtRange.svatky = [svatek]
        index = dtRange.kolikaty(datetime.strptime("2015-10-09", "%Y-%m-%d"))
        self.assertEqual(6,index)

    def test_kolikaty_before(self):
        """Between 1.10.2015 and 31.10.2015 30.09.2015 should be index=-1"""   
        dtFrom = datetime.strptime("2015-10-01", "%Y-%m-%d")
        dtTo = datetime.strptime("2015-10-31", "%Y-%m-%d")
        dtRange = DateRange(dtFrom,dtTo)
        svatek = datetime.strptime("2015-10-28", "%Y-%m-%d")
        dtRange.svatky = [svatek]
        index = dtRange.kolikaty(datetime.strptime("2015-09-30", "%Y-%m-%d"))
        self.assertEqual(-1,index)
        
    def test_kolikaty_after(self):
        """Between 1.10.2015 and 31.10.2015 02.11.2015 should be index=-2"""   
        dtFrom = datetime.strptime("2015-10-01", "%Y-%m-%d")
        dtTo = datetime.strptime("2015-10-31", "%Y-%m-%d")
        dtRange = DateRange(dtFrom,dtTo)
        svatek = datetime.strptime("2015-10-28", "%Y-%m-%d")
        dtRange.svatky = [svatek]
        index = dtRange.kolikaty(datetime.strptime("2015-11-02", "%Y-%m-%d"))
        self.assertEqual(-2,index)
        

if __name__ == "__main__":
    unittest.main()
    
    
