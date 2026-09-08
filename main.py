TOKEN_RULES = {
    "attendance": 1,
    "homework": 1,
    "extraordinary": 1,
    "bad_behavior": -1,
    "no_practice": -1,
    "small_reward": -5,
    "regular_reward": -20,
    "big_reward": -45,
}

students = {
    "Test Student": 0,
}

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
    student = input("Student name (or 'quit' to exit): ")
    if student.lower() == "quit":
        break 
    rule = input("Rule: ")
    apply_rule(student, rule)