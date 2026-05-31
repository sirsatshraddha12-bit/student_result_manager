from random import choice


student = {}

while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Student")
    print("2.Check Result")
    print("3. Exit")
    
    choice = input("Enter your choice:")
    
    #Add Student
    if choice == "1":        
        name = input("Enter student name:")
        mark = int(input("Enter student marks:"))
        student[name] = mark
        print(f"{name} added successfully!")
        
    elif choice =="2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)
                
    elif choice == "3":
        name = input("Enter student name:")
        
        if name in student:
            marks = student[name]
            if marks >= 40:
                print(f"{name} has passed with marks {marks}.")
            else:
                print(f"{name} has failed with marks {marks}.")
                
        else:
            print("Student Not Found!")
            
    elif choice == "4":
        print("Exiting....")
        break
    else:       
        print("Invalid choice! Please try again.")