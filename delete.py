
def delete_student():
    sid=input("enter student id to delete:")
    for s in students:
        if s['id']==sid:
            students.remove(s)
            print("student deleted sucessfully")
            return
        print("student not found")
delete_student()

