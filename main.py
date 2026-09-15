import json

TOKEN_RULES = {
    "setup": 0,
    "attendance": 1,
    "homework": 1,
    "extraordinary": 1,
    "bad_behavior": -1,
    "no_practice": -1,
    "small_reward": -5,
    "regular_reward": -20,
    "big_reward": -45,
}

def sort_students():
    global students 
    sorted_students = {}
    for student in sorted(students):
        sorted_students[student] = students[student]
    students = sorted_students

try: 
    with open("students.json", "r") as f:
        students = json.load(f)
except FileNotFoundError:
    students = {}

sort_students()

print(students)

def apply_rule(student, rule):
    if rule not in TOKEN_RULES:
        print(rule,"is not a valid rule. Try again")
        return
    if student not in students:
        students[student] = 0
    students[student] += TOKEN_RULES[rule]
    print(f"{student}: {rule} ({TOKEN_RULES[rule]:+d}) -> new balance {students[student]}")

while True:
    print("\n1. Apply a rule\n2. View a student's balance\n3. List all students\n4. Quit")
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
            print(student, students[student])
    elif choice == "4":
        break
    else:
        print("Not a valid option, try again")

with open("students.json", "w") as f:
    json.dump(students, f)

print("Saved!")