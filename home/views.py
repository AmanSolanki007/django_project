from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is index")
   return render(request,'index.html')
    
def services(request):
    return render (request,'services.html')

def contact(request):
    return render (request,'contact.html')

def save(request):
    return render (request,'contact.html')
            
