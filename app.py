from flask import Flask,render_template,jsonify,request
from npmjournalist import npm_journalist

app= Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

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
