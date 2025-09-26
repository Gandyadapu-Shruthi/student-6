
def menu():
    while True:
        print("...student management system...")
        print("1.Add student")
        print("2.View student")
        print("3.Serach student")
        print("4.Update student")
        print("5.Delete student")
        print("6.Exit")
        choice=input("enter your choice here:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            search_student()
        elif choice=="4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            print("exit")
            break
        else:
            print("invalid")
menu()
