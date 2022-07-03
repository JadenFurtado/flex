from app import app
from flask import Flask,request
import json
from app import database
import requests

@app.route("/parser",methods=['GET'])
def parseRequest():
    #f = open("/home/jadenfurtado/Desktop/swag/download.json", "r")
    endpoint = request.args.get("endpoint")
    if endpoint==None:
        return "please enter the endpoint parameter in the URL"
    try:
        res = requests.get(url="http://localhost:3000/?endpoint="+endpoint)
        a = res.json()
        requests = a[0][0]
        schema = {"request":requests,"endpoint":endpoint}
        db = database.MyDatabase()
        db.insertSchema(schema)
        return "success"
    except:
        return "an error occurred"
    # parsedJsonData = json.loads(str(res.json()))
    # responseBody = list()
    # 
    # for a in parsedJsonData[0]:
    #     if a["response_headers"]["content-type"]=="application/coreapi+json" or a["response_headers"]["content-type"]=="application/openapi+json":# or a["reponse_headers"]["content-type"]=="application/openapi+json":
    #         responseBody.append(a)
    # if responseBody == None:
    #     return "No response from the endpoint"
    # else:
    #     schema = {"schema":responseBody}
    #     db.insertSchema(schema)
    #     return str(responseBody)
    #request.form.get("request")