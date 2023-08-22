from django.urls import path

from app import views
from app.views import hello, job_detail

urlpatterns = [
    path ('', hello),
    path('job/<id>', views.job_detail),
]