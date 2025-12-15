from django.shortcuts import render, HttpResponse, redirect
from . forms import Registerform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required
def home(request):
    return render (request ,"index.html")
  
  

def register_view(request):

    
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:   
     form = Registerform()
    context = {
        'form': form
    }
    return render(request,"register.html",context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })


    return render(request, "login.html")


@login_required 
def logout_view(request):
    logout(request)

    return redirect('login')



def delete_task(request,id):
    return HttpResponse("Deleted")