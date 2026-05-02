from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from supabase import create_client
import requests
import uuid
import math
import os

#FastAPI Initialistaion


app = FastAPI()

#Supabase Initialistaion


SUPABASE_URL= os.environ.get("SUPABASE_URL")
SUPABASE_KEY= os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#Health Check


@app.post("/")
def health_check():
    return "{response:Healthy}"
    
#Normal Complaint


@app.post("/normal_complaint")
def normal_complain(
    photo: str = Form(),
    lat: float = Form(),
    longt: float = Form(),
    description: str = Form()
):
  custom_location = (
      supabase.table("profiles")
      .select("email,lat,longt")
      .execute()
      )

  all_distance = []
  all_email = []

  for location in custom_location["data"]:
    latitude = location["lat"]
    longitude = location["longt"]
    email = location["email"]
    distance = distance_diff(lat=lat,longt=longt,latd=latitude,longtd=longitude)
    all_distance.append(distance)
    all_email.append(email)

  short_distance = min(all_distance)
  distance_index = all_distance.index(short_distance)
  email_index = all_email[distance_index]

  photo_prep = open(photo,"rb")
  photo_upload = (
      supabase.storage
      .from_("NPM-Journalist")
      .upload(
          file=photo_prep,
          path=f"complaints/{email_index}/{photo}",
          file_options={"cache-control": "3600", "upsert": "false"}
          )
      )
  
  photo_url = (
      supabase.storage
      .from_("NPM-Journalist")
      .get_public_url(f"public/{email_index}/{photo}")
      )
  photo_uri =  photo_url["publicURL"]
  
  complaint_post = (
      supabase.table("planets")
      .insert({"email":email_index, "complaints":description, "photo_url":photo_uri})
      .execute()
      )
  
  return complaint_post

#Distance Matrix

  
def distance_diff(lat,longt,latd,longtd):
  x_r_id = str(uuid.uuid4())
  x_c_id = str(uuid.uuid4())

  API_KEY = os.environ.get("OLA_MAPS_API")
  response= requests.get(
      "https://api.olamaps.io/routing/v1/distanceMatrix",

      headers={
      "x-request-id": x_r_id,
      "x-correlation-id": x_c_id
    },
    params={
      "origins": f"{lat},{longt}",
      "destinations": f"{latd},{longtd}",
      "mode": "driving",
      "route_preference": "fastest",
      "api_key": f"{API_KEY}"
    }
      )
  return response["rows"][0]["elements"][0]["distance"]

#Sign up


@app.post("/signup")
async def new_volunteer(
    name: str = Form(""),
    email: str = Form(""),
    password: str = Form(""),
    phone: str = Form(""),
    profession: str = Form(""),
    lat: str = Form(""),
    longt: str = Form(""),
    active: str = Form(""),
    passive: str = Form(""),
    jno: str = Form(""),
    jyes: str = Form(""),
    organistaion: str = Form(""),
    description: str = Form(""),
    photo: UploadFile = File(None)
):
  signup =  supabase.auth.sign_up(
      {
          "email":email,
          "password":password,
          }
      )
  
  foto = await photo.read()
  upload = (
      supabase.storage
      .from_("NPM-Journalist")
      .upload(
          file=foto,
          path=f"public/{name}.png",
          file_options={"cache-control": "3600", "upsert": "true"}
          )
      )
  
  photo_url_s = (
      supabase.storage
      .from_("NPM-Journalist")
      .get_public_url(f"public/{name}.png"
      )
      )

  insert_data = (
      supabase.table("profiles")
      .insert({"name": str(name), "email":str(email), "password":str(password), "profession":str(profession), 
               "lat":str(lat), "long":str(longt), "active":str(active), "passive":str(passive), "jno":str(jno), "jyes":str(jyes), "photo_url":str(photo_url_s), "organisation":str(organistaion),
               "description":str(description)})
      .execute()
      )
  print(insert_data)

  return insert_data

#Sign in 


@app.post("/signin")
def signin(
    email: str = Form(),
    password: str = Form()
):
  sign_in = supabase.auth.sign_in_with_password(
    {
        "email": email,
        "password": password,
    }
    )

  if sign_in["user"]["aud"]=="authenticated":
    user_data = (
        supabase.table("profiles")
        .select("id, name, email, profession, location, active, passive, jno, jyes, photo_url, organisation, description")
        .execute()
        )

    for person in user_data["data"]:
      if email==person["email"]:
        full_data =  person
        id = full_data["id"]
        name = full_data["name"]
        profession = full_data["profession"]
        location = full_data["location"]
        active = full_data["active"]
        passive = full_data["passive"]
        jno = full_data["jno"]
        jyes = full_data["jyes"]
        photo_url =  full_data["photourl"]
        organisation =  full_data["organisation"]
        description = full_data["description"]
    
    complaints_text = (
        supabase.table("complaints")
        .select("email","complaints","photo_url")
        .execute()
    )

    complaints=[]
    photo_complain_link = []

    for complaint in complaints_text["data"]:
      email_identi = complaint["email"]
      if email_identi==email:
        complaints_text = complaint["complaints"]
        photo_link_c = complaint["photo_url"]
        complaints.append(complaints_text)
        photo_complain_link.append(photo_link_c)
        
    
  return JSONResponse(content={
    "name": name,
    "profession": profession,
    "location": location,
    "active": active,
    "passive": passive,
    "jno": jno,
    "jyes": jyes,
    "photo_url": photo_url,
    "organisation": organisation,
    "description": description,
    "complaints": complaints,
    "photo_complain_link": photo_complain_link
})
