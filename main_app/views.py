from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Ticket, Tag
from .forms import CommentForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ticket-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def ticket_index(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets/index.html', {'tickets': tickets})


@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    comment_form = CommentForm()
    tags_ticket_doesnt_have = Tag.objects.exclude(id__in=ticket.tags.all().values_list('id'))
    return render(request, 'tickets/detail.html', {
        'ticket': ticket,
        'comment_form': comment_form,
        'tags': tags_ticket_doesnt_have,
    })


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title', 'description', 'priority', 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TicketUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ['title', 'description', 'priority', 'status']

    def test_func(self):
        return self.get_object().user == self.request.user


class TicketDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/tickets/'

    def test_func(self):
        return self.get_object().user == self.request.user


@login_required
def add_comment(request, ticket_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.ticket_id = ticket_id
        new_comment.save()
    return redirect('ticket-detail', ticket_id=ticket_id)


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = '__all__'


class TagList(LoginRequiredMixin, ListView):
    model = Tag


class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'color']


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = '/tags/'


@login_required
def associate_tag(request, ticket_id, tag_id):
    Ticket.objects.get(id=ticket_id).tags.add(tag_id)
    return redirect('ticket-detail', ticket_id=ticket_id)


@login_required
def remove_tag(request, ticket_id, tag_id):
    Ticket.objects.get(id=ticket_id).tags.remove(tag_id)
    return redirect('ticket-detail', ticket_id=ticket_id)