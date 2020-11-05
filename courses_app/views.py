from django.shortcuts import render, redirect
from .models import course, desc
from django.contrib import messages

def index(request):
  context = {
    'all_courses': course.objects.all()
  }
  
  if request.method == "POST":
    errors = course.objects.validator(request.POST)
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect('/')
    else:  
      course.objects.create(
        name = request.POST['name']
      )     
      desc.objects.create(
        content = request.POST['desc'],
        course = course.objects.get(name = request.POST['name'])
      )
      return redirect('/', context)

  return render(request, 'index.html', context)

def delete_confirm(request, course_id):
  context = {
    'course_delete': course.objects.get(id = course_id)
  }
  return render(request, 'delete.html', context)

def delete(request, course_id):
  to_delete = course.objects.get(id = course_id)
  to_delete.delete()
  return redirect('/')