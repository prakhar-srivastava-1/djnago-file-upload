from django.shortcuts import render  
from django.http import HttpResponse  
from .forms import UploadForm  

def handle_uploaded_file(f):  
    with open('media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def home(request):  
    if request.method == 'POST':  
        student = UploadForm(request.POST, request.FILES)  
        if student.is_valid():  
            new_upload = student.save()
            return HttpResponse("File uploaded successfuly")  
    
    else:  
        student = UploadForm()  
        return render(request,"home.html",{'form':student})  
