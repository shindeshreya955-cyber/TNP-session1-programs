# Encapsulation Example in Python

class Student:
    def __init__(self):
        self.__rollNo = 0
        self.__name = ""

    def setData(self, r, n):
        self.__rollNo = r
        self.__name = n

    def getRollNo(self):
        return self.__rollNo

    def getName(self):
        return self.__name

s = Student()
s.setData(101, "Shreya")

print("Roll No :", s.getRollNo())
print("Name :", s.getName())
