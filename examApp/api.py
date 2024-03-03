from .api import *
from examPH.buri import *
import os, requests, json


# GET https://kube.exams.buri.dev/api/v1/exams
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

# GET https://kube.exams.buri.dev/api/v1/exams/:uuid/sections/
def get_sections_list(bearer_token,uuid):
    
    SECTIONS_URL = EXAMS_URL + "/" + uuid + "/sections/"
    sections_data = []
    context = {}
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + bearer_token
    }
    
    response = requests.request("GET", SECTIONS_URL, headers=headers, data=payload)
    response_dict = json.loads(response.text)

    if response_dict:
        try:
            for data in response_dict:
                section_data = {}
                for key, value in data.items():
                    if value is not None:
                        section_data[key] = value
                        context[key] = value
                sections_data.append(section_data)        
        except Exception as e:
            print(str(e))
    
    return sections_data

# GET https://kube.exams.buri.dev/api/v1/sections/:uuid/items/
def get_items_list(bearer_token,uuid):
    
    ITEMS_URL = API_URL + "sections/" + uuid + "/items/"
    items_data = []
    items_uuid = []
    context = {}
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + bearer_token
    }
    
    response = requests.request("GET", ITEMS_URL, headers=headers, data=payload)
    response_dict = json.loads(response.text)

    if response_dict:
        try:
            for data in response_dict:
                item_data = {}
                for key, value in data.items():
                    if value is not None:
                        item_data[key] = value
                        context[key] = value
                        if key == 'uuid':  # Check if the key is 'uuid'
                            items_uuid.append(value)
                items_data.append(item_data)        
        except Exception as e:
            print(str(e))
    
    return items_data, items_uuid

# GET https://kube.exams.buri.dev/api/v1/items/:uuid/choices/
def get_choices_list(bearer_token,uuid):
    
    CHOICES_URL = API_URL + "items/" + uuid + "/choices/"
    choices_data = []
    context = {}
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + bearer_token
    }
    
    response = requests.request("GET", CHOICES_URL, headers=headers, data=payload)
    response_dict = json.loads(response.text)

    if response_dict:
        try:
            for data in response_dict:
                choice_data = {}
                for key, value in data.items():
                    if value is not None:
                        choice_data[key] = value
                        context[key] = value
                choices_data.append(choice_data)        
        except Exception as e:
            print(str(e))
    
    return choices_data