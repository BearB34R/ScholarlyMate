# ScholarlyMate

Allows students to create a personalized study schedule, set reminders for assignments and exams, and track progress on learning goals.

## Start:

### First access the virtual environment using the terminal to start developing:

For windows:

```
.\djangoenv\Scripts\activate
```

For Unix or MacOS:

```
source djangoenv/bin/activate
```

## Things you need to install:\

```
pip install django-admin-soft-dashboard
```

https://www.youtube.com/watch?v=9h9SC34tNNU

## How to start website locally:

```
python manage.py makemigrations
python manage.py migrate
```

#### Create the superuser/admin account

```
python manage.py createsuperuser
```

##### Follow the steps after running the command to create the super user

#### Start the application (development mode)

```
python manage.py runserver
```

Access the admin section in the browser: http://127.0.0.1:8000/

# Template documation:

https://docs.appseed.us/boilerplate-code/django-templates/soft-dashboard/#how-to-use-it

# How to edit template

./djangoenv/lib/admin_soft/

```
# This exists in ENV: LIB/admin_soft
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
   |    |    |-- base-fullscreen.html # Masterpage for Auth Pages
   |    |
   |    |-- pages/
   |         |-- index.html           # Dashboard page
   |         |-- profile.html         # Settings  Page
   |         |-- *.html               # All other pages
   |
   |-- ************************************************************************
```
