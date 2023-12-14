from django.shortcuts import render,redirect
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request,"home.html",{
        'count': count
    })

def signup(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,"registration/signup.html",{
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect('home')
@login_required
def new_check(request):
    return render(request,"new_check.html")

class NewCheck(LoginRequiredMixin,TemplateView):
    template_name = "new_check.html"