from planovacv2.core import project
from datetime import datetime
import unittest

class TestProject(unittest.TestCase):

    def setUp(self):
        self.projekt = self._create_project("project-1","2016-01-16","2016-05-02")
        engine = project.Engine()
        engine.name = "engine-1"
        job = self._create_job("job-1",10,"2016-02-01")
        job2 = self._create_job("job-2",5,"2016-02-04")
        job3 = self._create_job("job-3",15,"2016-03-04")
        engine.add_job(job)
        engine.add_job(job2)
        engine.add_job(job3)
        self.projekt.add_engine(engine)
        
    def test_hierarchy_creation(self):
        """Project has 1 engine and this engine has 3 jobs."""
        self.assertEqual(1,len(self.projekt))
        self.assertEqual("engine-1",self.projekt.engines[0].name)
        self.assertEqual(3,len(self.projekt.engines[0]))
        self.assertEqual("job-1",self.projekt.engines[0].jobs[0].name)

    def test_job_end_date(self):
        """Job started 1.4.2016 and took 10 days should end in 14.4.2016"""
        job = self._create_job("j-1",10,"2016-04-01")
        expected = datetime(2016,4,14)
        self.assertEqual(expected,job.end)
        

    def _create_project(self,name,dtFrom,dtTo):
        projekt = project.Project()
        projekt.name = name
        projekt.dtFrom = datetime.strptime(dtFrom, "%Y-%m-%d")
        projekt.dtTo = datetime.strptime(dtTo, "%Y-%m-%d")
        return projekt

        
    def _create_job(self,name,days,start,projekt=None):
        job = project.Job()
        job.name = name
        job.days = days
        job.start = datetime.strptime(start, "%Y-%m-%d")
        if projekt:
            job.project = projekt
        return job
        
