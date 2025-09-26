
def update_student():
    sid=input("enter student id to update:")
    for s in students:
        if s["id"]==sid:
            s["name"]=input("enter new name:")
            s["course"]=input("enter new course:")
            s["marks"]=input("enter new marks:")
            print("student updated sucessfully")
            return
        print("student id did not match")
#update_student()
