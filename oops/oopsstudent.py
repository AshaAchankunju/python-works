class Student:
    Roll_No: int
    name:str
    batch_no:int
    department:str
    
    def set_stud(self,Roll_No,name,batch_no,department):
        self.Roll_No=Roll_No
        self.name=name
        self.batch_no=batch_no
        self.department=department

    def display_stud(self):
        print(self.Roll_No,self.name,self.batch_no,self.department)

stud1=Student()
stud1.set_stud(1,"Anu",4,"cs")
stud1.display_stud()