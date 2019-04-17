from django.shortcuts import render
from django.http import HttpResponse
from . import serializers
from . import models
from rest_framework import viewsets, generics
# Create your views here.

def index(request):
    return HttpResponse("<h1>You have reached core folder index</h1>")

class TweetSerialView(viewsets.ModelViewSet):
    queryset=models.Tweet.objects.all()
    serializer_class = serializers.TweetSerializer

# class LikeSerialView(viewsets.ModelViewSet):
#     queryset=models.Like.objects.all()
#     serializer_class = serializers.LikeSerializer

# class CommentSerialView(viewsets.ModelViewSet):
#     queryset=models.Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
class FollowSerialView(viewsets.ModelViewSet):
    queryset=models.Follow.objects.all()
    serializer_class = serializers.FollowSerializer

from . import forms
def user_form(request):
    if request.method=="POST":
        form=forms.UserForm(request.POST)
        if form.is_valid():
            return HttpResponse('<h1>form submitted</h1>')
    else:
        form = forms.UserForm(initial={'name':'Abhishektest01'})
    context={
        'form':form
    }
    print("form else")
    return render(request,'userform.html',context)
