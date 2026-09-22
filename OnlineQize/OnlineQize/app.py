from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "Which language is used to structure a web page?",
        "options": ["CSS", "HTML", "JavaScript", "Python"],
        "answer": "HTML"
    },
    {
        "question": "Which language is used to style a web page?",
        "options": ["HTML", "CSS", "Python", "Java"],
        "answer": "CSS"
    },
    {
        "question": "Which language is mainly used to make web pages interactive?",
        "options": ["HTML", "CSS", "JavaScript", "SQL"],
        "answer": "JavaScript"
    },
    {
        "question": "Which framework is used in this project?",
        "options": ["Django", "React", "Flask", "Angular"],
        "answer": "Flask"
    },
    {
        "question": "Which method is commonly used to send form data to a Flask server?",
        "options": ["GET", "POST", "SEND", "PUSH"],
        "answer": "POST"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():

    score = 0

    for i, question in enumerate(questions):
        user_answer = request.form.get(f"question{i}")

        if user_answer == question["answer"]:
            score += 1

    total = len(questions)
    percentage = (score / total) * 100

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage
    )


if __name__ == "__main__":
    app.run(debug=True)