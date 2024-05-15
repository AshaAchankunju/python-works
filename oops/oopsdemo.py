class Employee:

    id:int
    name:str
    department:str
    salary:int

    def set_emp(self,id,name,dep,sal):
        self.id=id
        self.name=name
        self.department=dep
        self.salary=sal

    def display_emp(self):
        print(self.id,self.name,self.department,self.salary)

emp1=Employee()
emp1.set_emp(12,"Andrew","HR",50000)

emp2=Employee()
emp2.set_emp(15,"Steeve","Manager",100000)

emp1.display_emp()
emp2.display_emp()