from django.shortcuts import render
from .models import Ticket


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def ticket_index(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html', {'tickets': tickets})


def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'tickets/detail.html', {'ticket': ticket})