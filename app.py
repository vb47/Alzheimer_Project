from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/HomePage")


@app.route("/HomePage")
def HomePage():
    return render_template("main_template.html", Headline="Alzheimer Project Analysis")

@app.route("/Surveys")
def Surveys():
    return render_template("main_template.html", Headline ="Surveys")

@app.route("/Results")
def Results():
    return render_template("main_template.html", Headline ="Results")

@app.route("/Help")
def Help():
    return render_template("main_template.html", Headline ="Support")

