class StudentData:
    def __init__(self, studentName, rollNo, dbmsMarks, pythonMarks, cMarks, osMarks, cnMarks):
        self.name = studentName
        self.rollNo = rollNo
        self.dbmsMarks = dbmsMarks
        self.pythonMarks = pythonMarks
        self.cMarks = cMarks
        self.osMarks = osMarks
        self.cnMarks = cnMarks
 
    def printAllDetails(self):
        print(self.name,end=" ")
        print(self.rollNo,end=" ")
        print(self.dbmsMarks,end=" ")
        print(self.pythonMarks,end=" ")
        print(self.cMarks,end=" ")
        print(self.osMarks,end=" ")
        print(self.cnMarks,end=" ")
obj1 = StudentData("Harika" , "5A1" , 78 , 67 , 77 ,89 ,46)
obj1.printAllDetails()
print( )
obj2 = StudentData("Swapna" , "5A2" , 38 , 65 , 97 , 59 , 41)
obj2.printAllDetails()
print( )
obj3 = StudentData("Sushma" , "5A3" , 88 , 95 , 47 , 89 , 31)
obj3.printAllDetails()
print( )
