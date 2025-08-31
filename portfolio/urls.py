from django.urls import path
from .views import home_view, ProjectListView, ProjectDetailView, contact_view

urlpatterns = [
    path("", home_view, name="home"),  
    path("projects/", ProjectListView.as_view(), name="project_list"),  
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),  
    path("contact/", contact_view, name="contact"),  
]
