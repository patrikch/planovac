class DrawUnit:
    def __init__(self,id,text,asoc):
        self.id = id
        self.text = text
        self.associated = asoc        
        self.x_start = 0
        self.y_start = 0
        self.x_size = 0
        self.y_size = 0
        self.color = ""
        self.border = True        

class EngineDrawUnits:
    def __init__(self):
        self.units = []

    def add_unit(self,du):
        self.units.append(du)

    
