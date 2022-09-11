from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Request

class RequestFrom(ModelForm):
    class Meta:
        model = Request
        fields = "__all__"
        labels = {
            "name":"",
            "number":"",
            "address":""
        }
    
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Your Name"}),
            "number":forms.NumberInput(attrs={"class":"form-control", "placeholder":"Enter Your Number"}),
            "address":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Your Address"}),
        }