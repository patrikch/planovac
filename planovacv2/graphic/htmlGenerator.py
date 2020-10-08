
class HtmlGenerator:
    template = """<!doctype html>
<html>
<head>
  <meta charset='utf-8'>
  <title>Project - {0}</title>
  <style type='text/css'>
  {1}
  </style>
</head>
<body>
<div>Project - {0}</div>
<div>{2}</div>
</body>
</html>"""
    obj_template = "<span id='{0}' class='{1}' style='{2}'>{3}</span>"

    
    def __init__(self,start_x,start_y,pxPerUnit):
        self.start_x = start_x
        self.start_y = start_y
        self.pxPerUnit = pxPerUnit

    def create_html(self,axeUnits,jobUnits,project):
        #parametry templatu: 0-title stranky(jmeno projektu),1-style,2-kreslici projekty                
        html_axe = _get_draw_units_html(self.start_x + 1 * self.pxPerUnit,
                                        self.start_y + 1 * self.pxPerUnit,axeUnits)
        html_jobs = _get_draw_units_html(self.start_x + 1 * self.pxPerUnit,
                                         self.start_y + 6 * self.pxPerUnit,jobUnits)
        
        

    def _get_draw_units_html(self,start_x,start_y,units):
        html = ""
        for unit in units:
            html += self._get_one_draw_unit_html(start_x,start_y,unit)
        return html

    def _get_one_draw_unit_html(self,start_x,start_y,unit):        
        #parametry templatu: 0-id,1-class,2-style,3-text
        html = ""

        return html
        
        
