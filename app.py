from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///lottapispa"
db = SQLAlchemy(app)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/frontpage", methods=["POST"])
def front_page():
    return render_template("frontpage.html", name=request.form["name"])

@app.route("/register")
def register():
    add_new_user()
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

def add_new_user():
    user_type = request.form["who"]
    username = request.form["name"]
    password = request.form["password"]
    sql = "INSERT INTO Users (username, password, user_type) VALUES (:username, :password, :user_type)"
    db.session.execute(sql, {"username": username, "password": password, "user_type": user_type})
    db.session.commit()