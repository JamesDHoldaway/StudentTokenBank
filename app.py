from flask import Flask
from bank import students

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1>Student Token Bank</h1>"
    for student in students:
        html += f"<p>{student}: {students[student]}</p>"
    return html

if __name__ == "__main__":
    app.run(debug=True)