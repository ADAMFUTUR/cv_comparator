from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_cv, name='upload_cv'),
    path('compare/', views.compare_cvs, name='compare_cvs'),
]
