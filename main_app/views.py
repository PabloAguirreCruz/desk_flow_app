from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Ticket, Tag
from .forms import CommentForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def ticket_index(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html', {'tickets': tickets})


def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    comment_form = CommentForm()
    tags_ticket_doesnt_have = Tag.objects.exclude(id__in=ticket.tags.all().values_list('id'))
    return render(request, 'tickets/detail.html', {
        'ticket': ticket,
        'comment_form': comment_form,
        'tags': tags_ticket_doesnt_have,
    })


class TicketCreate(CreateView):
    model = Ticket
    fields = ['title', 'description', 'priority', 'status']


class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['title', 'description', 'priority', 'status']


class TicketDelete(DeleteView):
    model = Ticket
    success_url = '/tickets/'


def add_comment(request, ticket_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.ticket_id = ticket_id
        new_comment.save()
    return redirect('ticket-detail', ticket_id=ticket_id)


class TagCreate(CreateView):
    model = Tag
    fields = '__all__'


class TagList(ListView):
    model = Tag


class TagDetail(DetailView):
    model = Tag


class TagUpdate(UpdateView):
    model = Tag
    fields = ['name', 'color']


class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'


def associate_tag(request, ticket_id, tag_id):
    Ticket.objects.get(id=ticket_id).tags.add(tag_id)
    return redirect('ticket-detail', ticket_id=ticket_id)


def remove_tag(request, ticket_id, tag_id):
    Ticket.objects.get(id=ticket_id).tags.remove(tag_id)
    return redirect('ticket-detail', ticket_id=ticket_id)