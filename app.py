from flask import Flask
from bank import students

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1>Student Token Bank</h1>"
    html += "<table border='1'"
    html += "<tr><th>Student</th><th>Balance</th></tr>"
    for student in students:
        html += f"<tr><td>{student}</td><td>{students[student]}</td></tr>"
    html += "</table>"
    return html

if __name__ == "__main__":
    app.run(debug=True)