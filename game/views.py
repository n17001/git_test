from django.shortcuts import render
import time

def stage(request):
    return render(request,'stage.html')
def story_html(request):
    a = ['story1','story2','story3']
    d={
        'test':a,
    }
    return render(request,'story.html',d)
def game_html(request):
    d ={
           'attack':request.GET.get('attack')
       }
    return render(request,'game.html',d)
def head_html(request):
    return render(request,'head.html')
