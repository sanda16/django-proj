from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("<int:question_id>/", views.details, name='details'),
    path("<int:question_id>/results/", views.results, name='results'),
    path('owner', views.owner, name='owner'),
]
