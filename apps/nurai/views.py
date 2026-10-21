from django.shortcuts import render
from .models import Students

def index(request):
    students = Students.objects.all()
    return render(request, 'index.html', {'students': students})