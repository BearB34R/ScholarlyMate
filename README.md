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

- if you don't have it run "pip install virutalenv"

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

## To see admin

- add "/admin" to the end the end of the url
- login using your superuser account

<br />

