from django.shortcuts import HttpResponse,render
from home.models import Contact


# Create your views here.
def index(request):
    return render(request,"index.html")
def contact (request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        phonenumber = request.POST.get("phonenumber")
        city = request.POST.get("city")
        state = request.POST.get("state")
        

        
        contact = Contact(username=username, password=password, phonenumber=phonenumber, city=city, state=state)
        contact.save()


    return render(request,"contact.html")
def about (request):
    return render(request,"about.html")
def blog (request):
    return render(request,"blog.html")