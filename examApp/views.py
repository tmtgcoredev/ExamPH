from django.shortcuts import render

def home(request):
    """"""
    template_name = "main/home.html"
    context = {}
        
    return render(request, template_name, context)

def dashboard(request):
    template_name = "main/dashboard.html"
    context = {}
        
    return render(request, template_name, context)
def exams(request):
    template_name = "main/exams.html"
    context = {}
        
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
