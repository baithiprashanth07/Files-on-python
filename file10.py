class emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def display(self):
        print("{:5} {:20s} {:10.2f}".format(self.id,self.name,self.sal))
