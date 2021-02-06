from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from movieapp import forms
from  movieapp.models import MovieInfo
#Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the Movieapp index.")

def display(request):
    global form
    form=forms.MovieInfo()
    my_dict={'form':form}
    form=forms.MovieInfo(request.POST)
    return render(request,'movieapp/index.html', context=my_dict)

def display_list(request):
    Movie_Info=MovieInfo.objects.all()
    return render(request,'movieapp/Movie_list.html',{'movieinfo':Movie_Info})

def add_new_movie(request):
        #global
        form=forms.MovieResForms()
        if request.method=='POST':
            form=forms.MovieResForms(request.POST)
            if form.is_valid():
                print("\n\n**************  Okkkkk  ********************")
                form.save()
                print("Data Inserted Successfully\n")
                return redirect('/')
        return render(request,'movieapp/add_movie.html',{'form':form})

def about_us(request):
    return render(request,'movieapp/about.html')
