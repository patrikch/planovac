from planovacv2.core import daterange
import unittest
from datetime import datetime
from ddt import ddt, data

@ddt
class TestDateRange(unittest.TestCase):

    def setUp(self):
        dtFrom = datetime.strptime("2015-10-01", "%Y-%m-%d")
        dtTo = datetime.strptime("2015-10-31", "%Y-%m-%d")
        svatek = datetime.strptime("2015-10-28", "%Y-%m-%d")
        self.dtRange = daterange.DateRange(dtFrom,dtTo)
        self.dtRange.svatky = [svatek]
        
    def test_get_range_days(self):
        """Between 1.10.2015 and 31.10.2015 should be 21 working days"""   
        days = list(self.dtRange.get_range_days())
        self.assertEqual(21,len(days))

    @data(("2015-10-09",6),("2015-09-30",-1),("2015-11-02",-2))
    def test_kolikaty_generic(self,arg):
        """Between 1.10.2015 and 31.10.2015 should be index="""
        day = arg[0]
        expected = arg[1]
        print("for day " + str(day) + " is index=" + str(expected))
        index = self.dtRange.kolikaty(datetime.strptime(day, "%Y-%m-%d"))
        self.assertEqual(expected,index)

    def test_xdays_after_day_should_be_day(self):
        """Between 1.10.2015 and 31.10.2015 6th day is 2015-10-08"""
        start = datetime.strptime("2015-10-01", "%Y-%m-%d")
        result = self.dtRange.get_day(start,6)
        expected = datetime.strptime("2015-10-08", "%Y-%m-%d")
        self.assertEqual(expected,result)
        
    def test_calculate_without_dtTo(self):
        """Between 1.10.2015 and None 6th day is 2015-10-08"""
        dtFrom = datetime.strptime("2015-10-01", "%Y-%m-%d")
        svatek = datetime.strptime("2015-10-28", "%Y-%m-%d")
        self.dtRange = daterange.DateRange(dtFrom,None)
        self.svatky = [svatek]
        counter = 0
        day = None
        for d in self.dtRange.get_range_days():
            counter += 1
            if counter == 6:
                day = d
                break
        
        expected = datetime.strptime("2015-10-08", "%Y-%m-%d")
        self.assertEqual(expected,day)

    def test_range_has_end(self):
        """if range dtFrom != None -> range has end"""
        self.assertTrue(self.dtRange.has_end)

    def test_range_has_not_end(self):
        """if range dtFrom == None -> range has not end"""
        dtFrom = datetime.strptime("2015-10-01", "%Y-%m-%d")
        self.dtRange = daterange.DateRange(dtFrom,None)
        self.assertFalse(self.dtRange.has_end)

if __name__ == "__main__":
    unittest.main()
