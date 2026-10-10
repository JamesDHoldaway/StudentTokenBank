from flask import Flask, request, redirect, url_for
from bank import students, TOKEN_RULES, apply_rule, save_students

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1>Student Token Bank</h1>"
    html += "<table border='1'>"
    html += "<tr><th>Student</th><th>Balance</th></tr>"
    for student in students:
        html += f"<tr><td>{student}</td><td>{students[student]}</td></tr>"
    html += "</table>"
    html += "<form method='POST' action='/apply'>"
    html += "<select name='student'>"
    for student in students:
        html += f"<option value='{student}'>{student}</option>"
    html += "</select>"
    html += "<select name='rule'>"
    for rule in TOKEN_RULES:
        html += f"<option value='{rule}'>{rule}</option>"
    html += "</select>"
    html += "<input type='submit'>"
    html += "</form>"
    return html

@app.route("/apply", methods=["POST"])
def apply():
    student = request.form["student"]
    rule = request.form["rule"]
    apply_rule(student, rule)
    save_students()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)