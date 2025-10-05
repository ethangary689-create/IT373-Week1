# myapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Announcement

def home(request):
    return render(request, "home.html")

def announcements_list(request):
    announcements = Announcement.objects.all()
    return render(request, "announcements/list.html", {"announcements": announcements})

def announcements_detail(request, id):
    announcement = get_object_or_404(Announcement, pk=id)
    return render(request, "announcements/detail.html", {"announcement": announcement})
