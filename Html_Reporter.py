class collapsible_report:
    def __init__(self):
        pass
    # def import_file(self,filename):
    #     self.report_file=open(filename,'a')
    # def new_file(self,filename):
    #     self.report_file=open(filename,'w')
    def clear_dd_string(self):
        self.dd_string=''
    def closedown(self):
        closedown_sequence='\n\t\t<script>\n\t\tvar coll = document.getElementsByClassName("light_collapsible");\n\t\tvar i;\n\t\tfor (i = 0; i < coll.length; i++) {\n\t\t\tcoll[i].addEventListener("click", function() {\n\t\t\t\tthis.classList.toggle("active");\n\t\t\t\tvar content = this.nextElementSibling;\n\t\t\t\tif (content.style.display === "block") {\n\t\t\t\t\tcontent.style.display = "none";\n\t\t\t\t} else {\n\t\t\t\t\tcontent.style.display = "block";\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\t\t</script>\n\n\t\t<script>\n\t\tvar coll = document.getElementsByClassName("green_collapsible");\n\t\tvar i;\n\t\tfor (i = 0; i < coll.length; i++) {\n\t\t\tcoll[i].addEventListener("click", function() {\n\t\t\t\tthis.classList.toggle("active");\n\t\t\t\tvar content = this.nextElementSibling;\n\t\t\t\tif (content.style.display === "block") {\n\t\t\t\t\tcontent.style.display = "none";\n\t\t\t\t} else {\n\t\t\t\t\tcontent.style.display = "block";\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\t\t</script>\n\n\t\t<script>\n\t\tvar coll = document.getElementsByClassName("red_collapsible");\n\t\tvar i;\n\t\tfor (i = 0; i < coll.length; i++) {\n\t\t\tcoll[i].addEventListener("click", function() {\n\t\t\t\tthis.classList.toggle("active");\n\t\t\t\tvar content = this.nextElementSibling;\n\t\t\t\tif (content.style.display === "block") {\n\t\t\t\t\tcontent.style.display = "none";\n\t\t\t\t} else {\n\t\t\t\t\tcontent.style.display = "block";\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\t\t</script>\n\t\t<script>\n\t\tvar coll = document.getElementsByClassName("collapsible");\n\t\tvar i;\n\t\tfor (i = 0; i < coll.length; i++) {\n\t\t\tcoll[i].addEventListener("click", function() {\n\t\t\t\tthis.classList.toggle("active");\n\t\t\t\tvar content = this.nextElementSibling;\n\t\t\t\tif (content.style.display === "block") {\n\t\t\t\t\tcontent.style.display = "none";\n\t\t\t\t} else {\n\t\t\t\t\tcontent.style.display = "block";\n\t\t\t\t}\n\t\t\t});\n\t\t}\n\t\t</script>\n\t\t</body>\n\t\t</html>'
        self.f.write(closedown_sequence)
        self.f.close()
    def initialize(self,path):
        self.f = open(path,'w')
        init_sequence='\n<!DOCTYPE html>\n<html>\n<head>\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<style>table,th,td{border: 1px solid black;}\n.light_collapsible {\n\t\tbackground-color: #BABABA;\n\t\tcolor: black;\n\t\tcursor: pointer;\n\t\tpadding: 18px;\n\t\twidth: 100%;\n\t\tborder: none;\n\t\ttext-align: left;\n\t\toutline: none;\n\t\tfont-size: 15px;\t\t\n}\n\n.green_collapsible {\n\t\tbackground-color: #ADFCAD;\n\t\tcolor: black;\n\t\tcursor: pointer;\n\t\tpadding: 18px;\n\t\twidth: 100%;\n\t\tborder: none;\n\t\ttext-align: left;\n\t\toutline: none;\n\t\tfont-size: 15px;\t\t\n}\n.red_collapsible {\n\t\tbackground-color: #FF4646;\n\t\tcolor: black;\n\t\tcursor: pointer;\n\t\tpadding: 18px;\n\t\twidth: 100%;\n\t\tborder: none;\n\t\ttext-align: left;\n\t\toutline: none;\n\t\tfont-size: 15px;\t\t\n}\n.collapsible {\n\tbackground-color: #777;\n\tcolor: white;\n\tcursor: pointer;\n\tpadding: 18px;\n\twidth: 100%;\n\tborder: none;\n\ttext-align: left;\n\toutline: none;\n\tfont-size: 15px;\n}\n.active, .collapsible:hover {\n\tbackground-color: #555;\n}\n.content {\n\tpadding: 0 18px;\n\tdisplay: none;\n\toverflow: hidden;\n\tbackground-color: #f1f1f1;\n}\n</style>\n</head>\n<body>'
        self.f.write(init_sequence)
    def insert_single_dropdown(self,dropdown,css_class="collapsible"):
        title=dropdown[0]
        html=dropdown[1]
        html_string='<button type="button" class="'+css_class+'">'+title+'</button><div class="content">\n'
        html_string+=html
        html_string+='</div>'
        return html_string
    def multiple_dropdowns(self,dropdown_list):
        html_string=''
        for x in dropdown_list:
            html_string+=self.insert_single_dropdown((x[0],x[1]))
        return html_string
    def add_to_file(self,text):
        self.f.write(text)