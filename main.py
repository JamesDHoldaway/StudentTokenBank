from bank import students, apply_rule, save_students

print(students)

while True:
    print("\n1. Apply a rule\n2. View a student's balance\n3. List all students\n4. Remove student from list\n5. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        student = input("Student name: ")
        rule = input("Rule: ")
        apply_rule(student, rule)
    elif choice == "2":
        student = input("Enter student's name for balance: ")
        try: 
            print(students[student])
        except KeyError:
            print("No student on record")
    elif choice == "3":
        for student in students:
            print(student,"-",students[student])
    elif choice == "4":
        student = input("Enter student name for removal: ")
        confirm = input(f"Type CONFIRM to remove {student} from token bank: ")
        if confirm == "CONFIRM":
            try:
                students.pop(student)
                print(f"{student} removed successfully")
            except KeyError:
                print("No student on record")
    elif choice == "5":
        break
    else:
        print("Not a valid option, try again")

save_students()
print("Saved!")