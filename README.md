# ScholarlyMate

Allows students to create a personalized study schedule, set reminders for assignments and exams, and track progress on learning goals.

## Start:

### First access the virtual environment using the terminal:

For windows:

```
.\djangoenv\Scripts\activate
```

For Unix or MacOS:

```
source djangoenv/bin/activate
```

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
python manage.py runserver # default port 8000
```

Access the admin section in the browser: http://127.0.0.1:8000/

# Template documation:

https://docs.appseed.us/boilerplate-code/django-templates/soft-dashboard/#how-to-use-it
