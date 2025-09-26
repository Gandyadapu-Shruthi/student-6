students=[]
max_students=8
valid_courses=["cs","ece","it","mech","civil"]
def add_student():
    if len(students)>=max_students:
        print("cannot add more students.limit reached")
        return
    sid=input("enter student id here:")
    name=input("enter student name here:")
    course=input("enter course(cs/ece/it/mech/civil):")
    if course not in valid_courses:
        print("invalid course")
        return
    marks=input("enter marks here:")
    student={"id":sid,"name":name,"course":course,"marks":marks}
    students.append(student)
    print("student added sucessfully")
    
add_student()
