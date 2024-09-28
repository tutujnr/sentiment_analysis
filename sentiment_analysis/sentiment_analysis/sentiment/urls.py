from django.urls import path
from . import views

urlpatterns = [
    path('sentiment/', views.sentiment_analysis, name='sentiment_analysis'),
    path('upload/', views.upload_form, name='upload_form'),
]


