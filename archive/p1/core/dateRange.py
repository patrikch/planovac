from datetime import datetime
from datetime import timedelta
from db.sqliteDatabase import Database

class DateRange:
    def __init__(self,dtFrom,dtTo):
        self.dtFrom = dtFrom
        self.dtTo = dtTo
        self._svatky = []        

    def _read_svatky(self):
        #kdyz neni nastaveno nacti z db
        sql = "select day from svatek order by day"
        recs = Database().get_records(sql,[])
        for r in recs:
            self._svatky.append(datetime.strptime(r["day"], "%Y-%m-%d"))
            
    @property
    def svatky(self):
        if len(self._svatky) == 0:
            self._read_svatky()
        return self._svatky

    @svatky.setter
    def svatky(self,days):
        #days must be list
        if len(self._svatky) > 0:
            self._svatky.clear()
        self._svatky.extend(days)        
        
        
    def get_range_days(self):
        days = []
        start = self.dtFrom
        end = self.dtTo

        while start <= end:
            if start not in self.svatky and start.weekday() not in (5,6):
                days.append(start)

            start = start + timedelta(days=1)

        return days

    def kolikaty(self,dt):
        days = self.get_range_days()
        if dt < days[0]:
            return -1
        if dt > days[len(days)-1]:
            return -2

        if dt in days:
            index = days.index(dt)
            return index
        raise Exception("Datetime:" + str(dt) + " isnt in project days." )
                
    def get_day(self,start,days):
        lst = self.get_range_days()
        startIndex = lst.index(start)
        tmp=0
        while tmp < days and startIndex + tmp < len(lst):
            tmp += 1

        return lst[startIndex + tmp - 1]
        
        
        
