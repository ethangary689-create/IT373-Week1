from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {"title": "Home"})

def about(request):
    data = {
        "title": "About",
        "name": "Ethan Gary Muralla",
        "student_id": "2023-12570",
    }
    return render(request, "about.html", data)