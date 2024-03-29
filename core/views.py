from django.shortcuts import render,redirect
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.viewsets import ModelViewSet

from core.models import Bill, Plate
from core.serializers import BillSerializer, PlateSerializer

# Create your views here.
class BillModelViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class PlateModelViewSet(ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer


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

@login_required
def new_check(request):
    return render(request,"new_check.html")

class NewCheck(LoginRequiredMixin,TemplateView):
    template_name = "new_check.html"