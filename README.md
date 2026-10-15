# Employee Master Django App

A reusable Django app for employee record management. The included screens and
models cover employee profiles, personal contact details, education, work
experience, and employee documents.

## Included

- Employee profile CRUD pages
- Personal and emergency contact details
- Educational qualifications and experience history
- Employee document upload forms and views
- Django migrations and templates

This repository contains the Django app module in `employee_master/`, not a
complete Django project: it does not include `manage.py`, project settings,
authentication configuration, or a database. Add `employee_master` to an
existing Django project and include its URL configuration from that project's
root URLs.

## Requirements

The provided `requirements.txt` lists the packages used by this app. Install
them in the host Django project's virtual environment:

```bash
pip install -r requirements.txt
```

Add `employee_master` to `INSTALLED_APPS`, include its URL patterns, and run
the host project's migrations:

```python
from django.urls import include, path

urlpatterns = [
    path("employee-master/", include("employee_master.urls")),
]
```

```bash
python manage.py migrate
```

The app's views require the host project to provide a login URL named `login`.
Configure `MEDIA_ROOT` and `MEDIA_URL` in the host project to handle uploaded
files.

## Privacy and security

Employee records and uploaded documents may contain highly sensitive personal
information, including government identity documents, contact details, and
employment history. Use synthetic data for development, restrict access to
uploads, and never commit real employee data, documents, credentials, or local
database files to a public repository.
