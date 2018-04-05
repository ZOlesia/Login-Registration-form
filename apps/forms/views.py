# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'forms/index.html')
def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(index)
    else:
        new_user = User.objects.create(
            first_name = request.POST['first_name'], 
            last_name = request.POST['last_name'], 
            email = request.POST['email'], 
            password = request.POST['password'], 
            conf_password = request.POST['confirm']
        )
        request.session['user_id'] = new_user.id
        return redirect(success)
        
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(index)
    else:
        request.session['user_id'] = User.objects.get(email = request.POST['email']).id

        return redirect(success)


def success(request):
    context =  {
        'user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'forms/success.html', context)