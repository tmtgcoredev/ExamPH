from .api import *
from examPH.buri import *
import os, requests, json


# GET https://testing.exams.buri.dev/api/v1/exams
def get_exams_list(bearer_token):  
    exams_data = []
    context = {}
    payload={}
    headers = {
    'Authorization': 'Bearer ' + bearer_token
    }
    
    response = requests.request("GET", EXAMS_URL, headers=headers, data=payload)
    response_dict = json.loads(response.text)

    if response_dict:
        try:
            for data in response_dict:
                exam_data = {}
                for key, value in data.items():
                    if value is not None:
                        exam_data[key] = value
                        context[key] = value
                exams_data.append(exam_data)        
        except Exception as e:
            print(str(e))
    
    return exams_data
