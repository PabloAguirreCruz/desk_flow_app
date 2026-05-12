# DeskFlow

An IT help desk ticketing system built with Django. Submit tickets, track their status, tag them by category, and discuss them in threaded comments.

Final project for General Assembly's Software Engineering Immersive bootcamp.

## Features

- Create, view, edit, and delete support tickets
- Priority levels (Low / Medium / High) with color-coded display
- Status tracking (Open / In Progress / Resolved / Closed)
- Tag system with many-to-many relationships
- Threaded comments on each ticket
- Django admin for backend management

## Tech Stack

- **Backend:** Python 3.12, Django
- **Database:** SQLite (development), PostgreSQL (planned for production)
- **Frontend:** Django templates with vanilla CSS

## Getting Started

```bash
git clone https://github.com/YOUR-USERNAME/deskflow.git
cd deskflow
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

- `main_app/models.py` — Ticket, Tag, and Comment models
- `main_app/views.py` — Function and class-based views for all CRUD operations
- `main_app/urls.py` — URL routing
- `main_app/templates/` — Django templates with shared base layout

## Status

Active development. Built for bootcamp final project presentation.