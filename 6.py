def student_data(student_id, student_name='',student_class=''):
    print("SID-",student_id)
    if(student_name):
        print("Name-",student_name)
    if(student_class):
        print("Class-",student_class)
    print("----------")
sid1 = int(input("Enter student 1 ID"))
sid2 = int(input("Enter student 2 ID"))
student_data(sid1,"Himanshu","1st")
student_data(sid2)
    
