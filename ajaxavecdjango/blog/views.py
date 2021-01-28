# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.



class SignUpView(CreateView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm
