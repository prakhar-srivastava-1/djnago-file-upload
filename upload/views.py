import os
from django.shortcuts import render  
from django.http import HttpResponse  
from .forms import UploadForm  
from django.conf import settings

def handle_uploaded_file(f):  
    with open('media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def home(request):  
    if request.method == 'POST':  
        student = UploadForm(request.POST, request.FILES)  
        if student.is_valid():  
            new_upload = student.save()
            return HttpResponse("File uploaded successfuly <br><a href='show_files'>Show Files</a>")  
    
    else:  
        student = UploadForm()  
        return render(request,"home.html", {'form':student})  

def show_files(request):
    media_dir = settings.MEDIA_ROOT
    print(media_dir)
    file_list = os.listdir(settings.MEDIA_ROOT)
    return render(request, "show_files.html", {"file_list": file_list, "media_dir": media_dir})
