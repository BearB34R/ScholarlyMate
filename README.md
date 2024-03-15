# ScholarlyMate

Allows students to create a personalized study schedule, set reminders for assignments and exams, and track progress on learning goals.

## Start the app in Docker

The easiest way to start up btw if you have docker don't worry about this if you already did the manual

- if this is causing you trouble just use the manual build

```
docker-compose up --build
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Manual Build (Steps)

### 1. make Virtual environment:

```bash
virtualenv djangoenv
```

### 2. Start virtual environment:

#### For windows:

```
.\djangoenv\Scripts\activate
```

#### For Unix or MacOS:

```
source djangoenv/bin/activate
```

### 3. Run bash script <=========Made it easier for yalls

- this bash script installs all requirements and runs the manage.py

```
bash build.sh
```

<br />

### 4. Create the Superuser

```bash
python manage.py createsuperuser
```

<br />

### 5. 👉 Start the app

```bash
python manage.py runserver
```

the app runs at `http://127.0.0.1:8000/`.

<br />

## Codebase structure

```bash
< PROJECT ROOT >
   |
   |-- core/
   |    |-- settings.py                  # Project Configuration
   |    |-- urls.py                      # Project Routing
   |
   |-- home/
   |    |-- views.py                     # APP Views
   |    |-- urls.py                      # APP Routing
   |    |-- models.py                    # APP Models
   |    |-- tests.py                     # Tests
   |    |-- templates/                   # Theme Customisation
   |         |-- includes                #
   |              |-- custom-footer.py   # Custom Footer
   |
   |-- requirements.txt                  # Project Dependencies
   |
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to Customize

When a template file is loaded, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found.
The theme used to style this starter provides the following files:

```bash
# This exists in "djangoenv" director: ./djangoenv/LIB/admin_adminlte
< UI_LIBRARY_ROOT >
   |
   |-- templates/                     # Root Templates Folder
   |    |
   |    |-- accounts/
   |    |    |-- login.html           # Sign IN Page
   |    |    |-- register.html        # Sign UP Page
   |    |
   |    |-- includes/
   |    |    |-- footer.html          # Footer component
   |    |    |-- sidebar.html         # Sidebar component
   |    |    |-- navigation.html      # Navigation Bar
   |    |    |-- scripts.html         # Scripts Component
   |    |
   |    |-- layouts/
   |    |    |-- base.html            # Masterpage
   |    |    |-- base-auth.html       # Masterpage for Auth Pages
   |    |
   |    |-- pages/
   |         |-- index.html           # Dashboard Page
   |         |-- calendar.html        # Profile Page
   |         |-- *.html               # All other pages
   |
   |-- ************************************************************************
```

## Youtube tutorial:

https://www.youtube.com/watch?v=D8zaXFtVF2w

<br />

# Template Docs:

https://docs.appseed.us/products/django-dashboards/adminlte
