from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from BugTrackApp.models import custom_user, bug_ticket
from BugTrackApp.forms import new_ticket_form, login_form


@login_required
def index(request):
    tickets = bug_ticket.objects.all()
    return render(request, 'index.html', {'tickets': tickets})


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = new_ticket_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_bug_ticket = bug_ticket.objects.create(
                title = form.get('title'),
                description = form.get('description'),
                status = 'New',
                created_by = request.user,
                assigned = None,
                completed_by = None,
            )
            return HttpResponseRedirect('/')
    form = new_ticket_form
    return render(request, 'form.html', {'form': form})


@login_required
def ticket_details(request, ticket_id):
    ticket = bug_ticket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_details.html', {'ticket': ticket} )


@login_required
def edit_ticket(request,ticket_id):
    ticket = bug_ticket.objects.filter(id=ticket_id).first()
    if request.method == 'POST': 
        form = new_ticket_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
            return HttpResponseRedirect('/')
    data = {
        'title': ticket.title,
        'description': ticket.description,
    }
    form = new_ticket_form(initial=data)
    return render(request, 'form.html', {'form': form})


def claim_ticket(request, ticket_id):
    ticket = bug_ticket.objects.filter(id=ticket_id).first()
    if ticket.status == 'New':
        ticket.status = 'In Progress'
        ticket.assigned = request.user.username
        ticket.save()
        return HttpResponseRedirect('/')


def complete_ticket(request, ticket_id):
    ticket = bug_ticket.objects.filter(id=ticket_id).first()
    if ticket.status == 'In Progress':
        ticket.status = 'Done'
        ticket.assigned = None
        ticket.completed_by = request.user.username
        ticket.save()
        return HttpResponseRedirect('/')


def invalidate_ticket(request, ticket_id):
    ticket = bug_ticket.objects.filter(id=ticket_id).first()
    ticket.status = 'Invalid'
    ticket.assigned = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            user = authenticate(request, username=form.get('username'), password=form.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = login_form
    return render(request, 'form.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')