
def view_students():
    if not students:
        print("No student found")
        return
    print("ID\tName\tCourse\tMarks")
    print("-"*30)
    for s in students:
        print(f"{s['id']}\t{s['name']}\t{s['course']}\t{s['marks']}")
        print()

#view_students()


