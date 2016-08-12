from datetime import datetime
from datetime import timedelta

class DateRange:
    def __init__(self,dtFrom,dtTo):
        self.dtFrom = dtFrom
        self.dtTo = dtTo
        self.svatky = []

    @property
    def has_end(self):
        return self.dtTo != None

    def get_range_days(self,limit=100):
        start = self.dtFrom
        counter = 0
        while True:
            if self.has_end and start > self.dtTo:
                return

            if counter == limit:
                return
                
            if start not in self.svatky and start.weekday() not in (5,6):
                counter += 1
                yield start
            
            start = start + timedelta(days=1)

    def kolikaty(self,dt):
        i = iter(self.get_range_days())
        curr_dt = next(i)
        if dt < curr_dt:
            return -1
        index = 0
        while dt != curr_dt:
            curr_dt = next(i,None)
            if not curr_dt:
                return -2
            index += 1
            if self.has_end and self.dtTo < dt:
                return -2
            
        if curr_dt == dt:
            return index

        return -2
    
    def get_day(self,start,days):
        i = iter(self.get_range_days())
        curr_dt = next(i)
        while start != curr_dt:
            curr_dt = next(i,None)

        counter = 1
        while counter < days:
            curr_dt = next(i,None)
            counter += 1
            
        return curr_dt

    def __repr__(self):
        return "DateRange(dtFrom={0},dtTo={1})".format(str(self.dtFrom),str(self.dtTo))

if __name__ == "__main__":
    dr = DateRange(datetime(2016,4,1),datetime(2016,4,21))
    #for dt in dr.get_range_days(30):
    #    print(str(dt))
    #num = dr.kolikaty(datetime(2016,4,1))
    #print(str(num))
    dt = dr.get_day(datetime(2016,4,1),10)
    print(str(dt))
    #ls = list(dr.get_range_days())
    #for dt in ls:
    #    print(str(dt))
    print("done")
    


    


    
