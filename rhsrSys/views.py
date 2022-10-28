from django.http import HttpResponse
from django.shortcuts import render
from rhsrSys.functions import handle_uploaded_file  
from rhsrSys.forms import UploadForm  

# Create your views here.
def index(request):
    if request.method == 'POST':  
        student = UploadForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return render(request,"rhsrSys/recognize.html")
    else:  
        student = UploadForm()  
        return render(request,"rhsrSys/index.html",{'form':student})

def recognize(request):
    return HttpResponse('DOne')