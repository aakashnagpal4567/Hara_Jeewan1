from flask import Flask, render_template,request
from pymongo import MongoClient


app=Flask("Hara Jeewan")

@app.route("/")
def front():
    return render_template("First-Page.html")

@app.route("/home")
def home():
    return render_template("cropquery.html")

@app.route("/cropinfo",methods=["POST", "GET"])
def forms():
    s=request.form.get("crop")  
    s=str(s)
    print(s)
    print(type(s))
    client = MongoClient('mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    filter={
    'CROPS': s
}
    result = client['crops']['cropinfo'].find(
    filter=filter
     )
    print(type(result))
    rslt=list(result)
    print(type(rslt))
    cropname = rslt[0]["CROPS"]
    about = rslt[0]["GENERAL INFO"]
    croptype = rslt[0]["TYPE OF CROPS"]
    bio_name = rslt[0]["BIOLOGICAL NAMES"]
    seeds = rslt[0]["SEED"]
    soil = rslt[0]["TYPE OF SOIL USED"]
    major_g_states = rslt[0]["MAJOR GROWING STATES"]
    climate = rslt[0]["CLIMATE(degree)"]
    #irrigation = rslt[0]["SEED"]
    grow_months= rslt[0]["GROWING MONTHS"]
    yield_d = rslt[0]["YIELD (DAYS)"]
    pesticide = rslt[0]["PESTICIDE TYPE"]
    chemical = rslt[0]["CHEMICAL USED"]
    diseases = rslt[0]["Diseases"]
    symptoms = rslt[0]["Symptoms"]
    print(cropname)
    #return (cropname)
    return render_template("printcropinfo.html", cropname=cropname,about=about,croptype=croptype, bio_name=bio_name,seeds=seeds,soil=soil, 
    major_g_states=major_g_states,climate=climate,grow_months=grow_months,yield_d=yield_d,  pesticide=pesticide,
     chemical=chemical, diseases=diseases,symptoms=symptoms)

@app.route("/data")
def data():
    return "data123"

app.run(port=5000,debug=True)    