# DeskFlow

![DeskFlow screenshot](https://file%2B.vscode-resource.vscode-cdn.net/Users/dbapes/Desktop/Screenshot%202026-05-12%20at%202.47.26%E2%80%AFPM.png?version%3D1778611855296)

## About

DeskFlow is an IT help desk ticketing system built with Django. Users can sign up, submit support tickets, organize them by priority and status, categorize them with tags, and track progress through threaded comments. Each user has their own private workspace — only the ticket creator can edit, delete, or modify their tickets.

Built as the final project for General Assembly's Software Engineering Immersive bootcamp. I chose a help desk app because it touches every CRUD pattern in a domain that hiring managers actually recognize — and because every workplace has a help desk, the demo doesn't need explanation.

## Getting started

- **Live app:** https://deskflow-pablo-64cf2066fc84.herokuapp.com/
- **Planning materials:** https://trello.com/b/Bo9lD2bC/deskflow

To run locally:

```bash
git clone https://github.com/PabloAguirreCruz/desk_flow_app.git
cd deskflow
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Technologies used

- **Backend:** Python 3.11, Django 5.2
- **Database:** PostgreSQL (production), SQLite (development)
- **Frontend:** Django templates, vanilla CSS with Flexbox and Grid
- **Auth:** Django's built-in session-based authentication
- **Deployment:** Heroku with Gunicorn and WhiteNoise

## Features

- User signup, login, and logout
- Create, view, edit, and delete support tickets
- Priority levels (Low / Medium / High) with color-coded display
- Status tracking (Open / In Progress / Resolved / Closed)
- Tag system with many-to-many relationships
- Threaded comments on each ticket
- Per-user data isolation — users only see and edit their own tickets
- Responsive grid layout for the ticket list

## Next steps

- File attachments on tickets via Cloudinary
- Email notifications when a ticket status changes
- Multi-user roles (technician vs. requester) with assignment workflows
- Dashboard showing ticket counts by status and priority
- Full-text search across tickets and comments
- Dark mode toggle