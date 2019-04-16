from django.shortcuts import render

# Create your views here.
def user_home(request):
    print("user_home")
    return render(request,template_name="index.html")

def user_login(request):
    print("user_login")
    return render(request,template_name="login.html")
def user_logout(request):
    print("user_logout")
    return render(request,template_name="logged_out.html")
def user_signup(request):
    return render(request,template_name="signup.html")