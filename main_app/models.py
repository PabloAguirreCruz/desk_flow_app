from django.db import models
from django.urls import reverse

PRIORITIES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

STATUSES = (
    ('O', 'Open'),
    ('P', 'In Progress'),
    ('R', 'Resolved'),
    ('C', 'Closed'),
)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, default='gray')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.id})


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    priority = models.CharField(max_length=1, choices=PRIORITIES, default=PRIORITIES[1][0])
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUSES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'ticket_id': self.id})


class Comment(models.Model):
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on {self.ticket.title} at {self.created_at}"

    class Meta:
        ordering = ['-created_at']