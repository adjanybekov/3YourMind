#-*- coding: utf-8 -*-
from django import forms

from django import forms

class ProfileImageForm(forms.Form):
    myfile = forms.FileField()