from datetime import timedelta

#object job potrebuje mit engine(id-int),start(datetime),row(int),end(datetime)-potrebuje days a
#dtFrom a dtTo projektu
class RowsLocator:
    def assing_row(self,jobs,engine):
        """Set all jobs of one engine appropriate row(index)"""
        #select only jobs of this engine
        sel_jobs = [j for j in jobs if j.engine == engine]
        #vynuluj row
        for j in sel_jobs:
            j.row = 0
        #postupne prirazuj
        row = 1
        while self._all_are_assign(sel_jobs) != True:
            fst = self._find_first(sel_jobs,row)
            if self._all_are_assign(sel_jobs):
                break
            self._find_next(sel_jobs,row,fst)
            row += 1
        return row

    def _all_are_assign(self,jobs):
        lst = [ j for j in jobs if j.row == 0 ]
        return len(lst) == 0

    def _find_first(self,rest,row):
        """najde prvni vyhovujici ktery ma row=0 a nejnizsi start"""
        ls = [ j for j in rest if j.row == 0 ]
        if len(ls) == 0:
            return None
    
        ls.sort(key = lambda x: x.start)
        ls[0].row = row
        return ls[0]

    def _find_next(self,rest,row,lastJob):
        """najde dalsi job, kde j.start > lastJob.end, ten kde je nejmensi rozdil j.start-lastJob.end """
        #vsechny vyhovujici j.row == 0 and j.start > lastJob.end
        potential = [ j for j in rest if j.row == 0 and j.start > lastJob.end ]
        if len(potential) == 0:
            return
        #najdi job s nejmensim rozdilem j.start-lastJob.end (ve dnech,cas neni k dispozici)
        #1.najdi min.rozdil
        minDiff = min([j.start - lastJob.end for j in potential])
        #2.najdi joby,ktere maji tento rozdil
        sel = [j for j in potential if j.start - lastJob.end == minDiff]
        if len(sel) == 0:
            return
        sel[0].row = row
        self._find_next(rest,row,sel[0])    
    
