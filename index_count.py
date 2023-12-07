from itertools import count  
class employee:
    objectscount = count(0)
    index =0
    empid = 0
    empname = ''
    empadress = ''
    empsalary = 0


    def __init__(self):
        self.index = next(self.objectscount)
        
        
    def getdata(self):
        return str(self.empid) +";"+ self.empname + ";" + self.empadress + ";" + str(self.empsalary)

    def printdata(self):
        print(self.getdata())

emp1 = employee()
emp2 = employee()
emp3 = employee()

print(emp1.index)
print(emp2.index)
print(emp3.index)


print(emp2.objectscount)
