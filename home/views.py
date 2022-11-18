from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    
    context={

    }

    return render(request, 'login.html', context)

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("dashboard")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})

def logout_view(request):
    logout(request)
    redirect(request, 'home')

def dashboard(request):

  return render(request, 'index.html')
