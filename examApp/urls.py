from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('exams/', views.exams, name='exams'),
    path('podcast/', views.podcast, name='podcast'),
    path('review/', views.review, name='review'),
    path('leaderboards/', views.leaderboards, name='leaderboards'),
]