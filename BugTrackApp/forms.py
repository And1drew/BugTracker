from BugTrackApp.models import custom_user
from django import forms


class login_form(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)


class new_ticket_form(forms.Form):
    title = forms.CharField(max_length = 80)
    description = forms.CharField(widget=forms.Textarea)