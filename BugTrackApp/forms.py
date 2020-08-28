from BugTrackApp.models import custom_user
from django import forms


class login_form(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)


class new_ticket_form(forms.Form):
    title = forms.CharField(max_length = 80)
    description = forms.CharField(widget=forms.Textarea)
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid'),
    ]
    # status = forms.ChoiceField(choices=STATUS_CHOICES, initial='New')
    # assigned = forms.ModelChoiceField(queryset = custom_user.objects.all(), blank = True, initial = None)
    # created_by = forms.ForeignKey(custom_user, on_delete=forms.DO_NOTHING)
    # date = forms.DateTimeField(default=datetime.now)
    # completed = forms.CharField(default = None, null = True, max_length = 30)