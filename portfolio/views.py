from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Project, Skill
from .forms import ContactForm

def home_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, "portfolio/layout/home.html", {"projects": projects, "skills": skills})

class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/layout/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/layout/project_detail.html"
    context_object_name = "project"


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "portfolio/layout/contact.html", {"form": form})
