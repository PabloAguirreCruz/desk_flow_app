from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('tickets/', views.ticket_index, name='ticket-index'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket-detail'),
    path('tickets/create/', views.TicketCreate.as_view(), name='ticket-create'),
    path('tickets/<int:pk>/update/', views.TicketUpdate.as_view(), name='ticket-update'),
    path('tickets/<int:pk>/delete/', views.TicketDelete.as_view(), name='ticket-delete'),
    path('tickets/<int:ticket_id>/add-comment/', views.add_comment, name='add-comment'),
    path('tickets/<int:ticket_id>/associate-tag/<int:tag_id>/', views.associate_tag, name='associate-tag'),
    path('tickets/<int:ticket_id>/remove-tag/<int:tag_id>/', views.remove_tag, name='remove-tag'),

    path('tags/', views.TagList.as_view(), name='tag-index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]