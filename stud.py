# Student Management System using List

# Initial student database (list of lists)
stud = [ 
    [101, "Ram", 98],
    [102, "Sita", 88],
    [103, "Ramu", 78],
    [104, "Gita", 99]
]

# Infinite loop for menu system
while True:
    print("\nWelcome To Student Management System")
    print("1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Topper")
    print("6. Exit")

    # User choice input
    choice = int(input("Enter your choice: "))

    # Match case for operations
    match choice:

        # Add Student
        case 1:
            n = int(input("How many students do you want to add? "))

            for i in range(n):
                sid = int(input("Enter ID: "))
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))

                # Add new student to list
                stud.append([sid, name, marks])
                print(f"Student {i+1} added")

        # View Students
        case 2:
            print("\nID\tName\tMarks")

            # Display all students
            for i in stud:
                print(i[0], "\t", i[1], "\t", i[2])

        # Update Student
        case 3:
            sid = int(input("Enter student ID: "))

            # Search student by ID
            for i in stud:
                if sid == i[0]:

                    print("1. Update Marks")
                    print("2. Update Name")
                    print("3. Update All Details")
                    print("4. Exit")

                    ch = int(input("Enter your choice: "))

                    # Update marks
                    if ch == 1:
                        new_marks = int(input("Enter new marks: "))
                        i[2] = new_marks
                        print("Marks updated successfully!")

                    # Update name
                    elif ch == 2:
                        new_name = input("Enter new name: ")
                        i[1] = new_name
                        print("Name updated successfully!")

                    # Update full details
                    elif ch == 3:
                        i[1] = input("Enter new name: ")
                        i[2] = int(input("Enter new marks: "))
                        print("Details updated successfully!")

                    break

        # Delete Student
        case 4:
            sid = int(input("Enter student ID to delete: "))

            # Search and remove student
            for i in stud:
                if sid == i[0]:
                    stud.remove(i)
                    print("Student deleted successfully!")
                    break

        # Topper Student
        case 5:
            if len(stud) > 0:

                # Assume first student is topper
                topper = stud[0]

                # Find highest marks student
                for i in stud:
                    if i[2] > topper[2]:
                        topper = i

                print("\nTopper Details")
                print("ID:", topper[0])
                print("Name:", topper[1])
                print("Marks:", topper[2])

            else:
                print("No student data available!")

        # Exit program
        case 6:
            print("Thank You!")
            break

        # Invalid choice handling
        case _:
            print("Invalid Choice!")
