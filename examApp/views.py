from .api import *
from django.shortcuts import render
import jwt


def authenticate_user(request):
    request.session["user_token"] = "56fe7e75753ec844f4f774600aa05415f13c6348f9f2f5b8779a2e29645188905c2de8e78e5c20fb927846ed83128ddf9508e729e4fab55cf45c2c74b11adbd1"
    request.session.modified = True
    # try:
    #     for key, value in request.session.items():
    #         print('{}: {}'.format(key, value))
                 
    #     try:   
    #         user_token = request.session['user_token'] 
    #         payload = jwt.decode(user_token, API_SECRET_KEY, algorithms=['HS256'])

    #         # SAVE JWT PAYLOAD INTO SESSIONS
    #         for key,value in payload.items():
    #             if key == 'data':
    #                 for key,value in payload['data'].items():
    #                     if request.session[key]:
    #                         pass
    #                     else:
    #                         request.session[key] = value
    #                         request.session.modified = True
    #         return True
        
    #     except jwt.ExpiredSignatureError:
    #         # signout(request)
    #         return False
        
    # except KeyError:
    #     # signout(request)
    #     return False

def dashboard(request):
    template_name = "main/dashboard.html"
    context = {}    
        
    return render(request, template_name, context)
def exams(request):
    template_name = "main/exams.html"
    context = {}
    authenticate_user(request)
    user_token = request.session['user_token']
    
    context['exams_data'] = get_exams_list(user_token)
    
    return render(request, template_name, context)

def podcast(request):
    template_name = "main/podcast.html"
    context = {}
        
    return render(request, template_name, context)

def review(request):
    template_name = "main/review.html"
    context = {}
        
    return render(request, template_name, context)

def leaderboards(request):
    template_name = "main/leaderboards.html"
    context = {}
        
    return render(request, template_name, context)
