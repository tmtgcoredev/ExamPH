from .api import *
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import jwt


def authenticate_user(request):
    # request.session["user_token"] = "user_token"
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
def home(request):
    template_name = "index.html"
    return render(request, template_name)

def dashboard(request):
    template_name = "main/dashboard.html"
    context = {}  
    authenticate_user(request)
    user_token = request.session['user_token']
    
    all_exams_data = get_exams_list(user_token)
    paginator = Paginator(all_exams_data, 10)
    page = request.GET.get('page')
    
    try:
        exams_data = paginator.page(page)
    except PageNotAnInteger:
        exams_data = paginator.page(1)
    except EmptyPage:
        exams_data = paginator.page(paginator.num_pages)
        
    context['exams_data'] = exams_data  
        
    return render(request, template_name, context)
def exams(request):
    template_name = "main/exams.html"
    context = {}
    authenticate_user(request)
    user_token = request.session['user_token']
    
    all_exams_data = get_exams_list(user_token)
    paginator = Paginator(all_exams_data, 10)
    page = request.GET.get('page')
    
    try:
        exams_data = paginator.page(page)
    except PageNotAnInteger:
        exams_data = paginator.page(1)
    except EmptyPage:
        exams_data = paginator.page(paginator.num_pages)
        
    context['exams_data'] = exams_data
    
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
