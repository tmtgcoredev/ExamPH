from .api import *
from ExamApp.buri import *
import os, requests, json


# GET https://testing.exams.buri.dev/api/v1/applications
def applications(token):

  payload = {}
  headers = {
    # 'Authorization': 'Bearer 56fe7e75753ec844f4f774600aa05415f13c6348f9f2f5b8779a2e29645188905c2de8e78e5c20fb927846ed83128ddf9508e729e4fab55cf45c2c74b11adbd1'
    'Authorization': 'Bearer '+ token
  }

  response = requests.request("GET", APPLICATIONS_URL, headers=headers, data=payload)
  response_dict = json.loads(response.text)
  
  print(response.text)
