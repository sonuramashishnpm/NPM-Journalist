from flask import Flask,render_template,jsonify,request
from npmjournalist import npm_journalist
import requests
import os

app= Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")


#Normal Complaints

@app.route("/normal_complaints", methods=["POST"])
def normal_complaints():
    lat         = request.form.get("latitude", "")
    longt       = request.form.get("longitude", "")
    description = request.form.get("description", "")
    photo_file  = request.files.get("problem_image")

    api_uri = "https://sonuramashishnpm-npm-journalist.hf.space/normal_complaint"

    params = {
        "lat": lat,
        "longt": longt,
        "description": description
    }

    files = {}
    if photo_file:
        files["photo"] = (photo_file.filename, photo_file.read(), photo_file.content_type)

    response = requests.post(api_uri, params=params, files=files, timeout=1200)
    return jsonify(response.json())

#New Volunteer

@app.route("/signup", methods=["POST"])
def new_volunteer():
    name        = request.form.get("name", "")
    email       = request.form.get("email", "")
    password    = request.form.get("password", "")
    phone       = request.form.get("phone", "")
    profession  = request.form.get("profession", "")
    lat         = request.form.get("lat", "")
    longt       = request.form.get("longt", "")
    active      = request.form.get("active", "")
    passive     = request.form.get("passive", "")
    jno         = request.form.get("jno", "")
    jyes        = request.form.get("jyes", "")
    description = request.form.get("description", "")
    organisation= request.form.get("organisation", "")
    photo_file  = request.files.get("photo")

    api_uri = "https://sonuramashishnpm-npm-journalist.hf.space/signup"

    params = {
        "name": name, "email": email, "password": password,
        "phone": phone, "profession": profession,
        "lat": lat, "longt": longt,
        "active": active, "passive": passive,
        "jno": jno, "jyes": jyes,
        "description": description, "organisation": organisation
    }

    files = {}
    if photo_file:
        files["photo"] = (photo_file.filename, photo_file.read(), photo_file.content_type)

    response = requests.post(api_uri, data=params, files=files, timeout=1200)
    return jsonify(response.json())


#Sign in


@app.route("/signin", methods=["POST"])
def signin():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    api_uri = "https://sonuramashishnpm-npm-journalist.hf.space/signin"

    response = requests.post(api_uri, params={
        "email": email,
        "password": password
    }, timeout=1200)

    return jsonify(response.json())

#Anonymous Complaint

@app.route("/send_complain",methods=["POST"])
def data():
  data=request.get_json()
  officer=data.get("officer","")
  subject=data.get("subject","")
  body=data.get("body","")

  npm=npm_journalist(
      officer=officer,
      subject=subject,
      body=body,
  )
  npm.npmai()
  return jsonify({"response":"Email Sent Sucessfully We are also working on proving you a link from where you can track your complain and response"})


if __name__=="main":
  port=int(os.environ.get("PORT",5000))
  app.run(host="0.0.0.0", port=port, debug=False)
