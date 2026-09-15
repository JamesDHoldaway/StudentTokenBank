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

try: 
    with open("students.json", "r") as f:
        students = json.load(f)
except FileNotFoundError:
    students = {}

def sort_students():
    global students 
    sorted_students = {}
    for student in sorted(students):
        sorted_students[student] = students[student]
    students = sorted_students

sort_students()

def apply_rule(student, rule):
    if rule not in TOKEN_RULES:
        print(rule, "is not a valid rule. Try again")
        return
    if student not in students:
        students[student] = 0
    students[student] += TOKEN_RULES[rule]
    print(f"{student}: {rule} ({TOKEN_RULES[rule]:+d}) -> new balance {students[student]}")

def save_students():
    with open("students.json", "w") as f:
        json.dump(students, f)