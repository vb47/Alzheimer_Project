from flask import Flask, render_template, redirect

app = Flask(__name__, template_folder = "Templates")

@app.route("/")
def index():
    return redirect("/HomePage")


@app.route("/HomePage")
def HomePage():
    return render_template("home.html")

@app.route("/Surveys")
def Surveys():
    return render_template("survey.html")

@app.route("/Results")
def Results():
    return render_template("result.html")

@app.route("/Help")
def Help():
    return render_template("help.html")

@app.route("/Feedback")
def Feedback():
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)