# ScholarlyMate

Allows students to create a personalized study schedule, set reminders for assignments and exams, and track progress on learning goals.

## Start the app in Docker

The easiest way to start up btw if you have docker

```bash
$ docker-compose up --build
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Manual Build

### Start Virtual environment:

#### For windows:

```
.\djangoenv\Scripts\activate
```

#### For Unix or MacOS:

```
source djangoenv/bin/activate
```

### 👉 Run bash script <=========Made it easier for yalls

```
bash build.sh
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
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
   |-- env.sample                        # ENV Configuration (default values)
   |-- manage.py                         # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to Customize

When a template file is loaded, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found.
The theme used to style this starter provides the following files:

```bash
# This exists in ENV: LIB/admin_adminlte
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

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path.

> For instance, if we want to **customize the footer.html** these are the steps:

- ✅ `Step 1`: create the `templates` DIRECTORY inside the `home` app
- ✅ `Step 2`: configure the project to use this new template directory
  - `core/settings.py` TEMPLATES section
- ✅ `Step 3`: copy the `footer.html` from the original location (inside your ENV) and save it to the `home/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_adminlte/template/includes/footer.html`
  - Destination PATH: `<PROJECT_ROOT>home/templates/includes/footer.html`

> To speed up all these steps, the **codebase is already configured** (`Steps 1, and 2`) and a `custom footer` can be found at this location:

`home/templates/includes/custom_footer.html`

By default, this file is unused because the `theme` expects `footer.html` (without the `custom-` prefix).

In order to use it, simply rename it to `footer.html`. Like this, the default version shipped in the library is ignored by Django.

In a similar way, all other files and components can be customized easily.

<br />

# Template Docs:

https://docs.appseed.us/products/django-dashboards/adminlte
