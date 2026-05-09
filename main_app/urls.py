from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tickets/', views.ticket_index, name='ticket-index'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket-detail'),
]