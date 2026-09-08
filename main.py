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
    students[student] += TOKEN_RULES[rule]
    print(f"{student}: {rule} ({TOKEN_RULES[rule]:+d}) -> new balance {students[student]}")

apply_rule("Test Student", "attendance")
apply_rule("Test Student", "no_practice")