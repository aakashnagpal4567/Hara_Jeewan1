from flask import Flask, render_template,request

app=Flask("work")

app.route("/home1")
def new():
    return "hello"
    #return render_template("index.html")

app.route("/new")
def home():
    s=request.args.get("crop")
    print(s)
    print(type(s))
    return s

app.run(port=5000,debug=True) 