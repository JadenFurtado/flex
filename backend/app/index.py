from app import app
from flask import Flask
from flask import request,render_template

@app.route("/",methods=["GET"])
def home():
    print(request.form.get('request'))
    return "Hello, World!"

@app.route("/sample",methods=["GET"])
def getSampleSchema():
    return render_template("sample.html")
#