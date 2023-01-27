class Student:
    pass
class Marks:
    pass
std = Student()
mks = Marks()
print(isinstance(std,Student))
print(isinstance(mks,Marks))
print(issubclass(Student,object))
print(issubclass(Marks,object))

