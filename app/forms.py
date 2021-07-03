from django import forms

class Contactformemail(forms.Form):
    email  = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message =  forms.CharField(required=True)

    