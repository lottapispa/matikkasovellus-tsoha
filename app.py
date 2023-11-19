from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/frontpage", methods=["POST"])
def front_page():
    return render_template("frontpage.html", name=request.form["name"])

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login_after_register():
    return render_template("login.html", name=request.form["name"])

@app.route("/elementary-math")
def elementary_math():
    return render_template("elementary-math.html")

@app.route("/addition")
def addition():
    return render_template("addition.html")

@app.route("/el-math-statistics")
def statistics():
    return render_template("el-math-statistics.html")