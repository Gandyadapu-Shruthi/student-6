
def search_student():
    sid=input("enter student id to search:")
    for s in students:
        if s['id']==sid:
            print(f"id:{s['id']},name:{s['name']},course:{s['course']},marks:{s['marks']}")
            return
    print("student not found")
search_student()

