from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def user_home(request):
    print("user_home")
    return render(request,template_name="index.html")

def user_logout(request):
    if request.method == "POST":
        logout(request)
    return redirect('login')

    
class SignUp(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name="signup.html"
