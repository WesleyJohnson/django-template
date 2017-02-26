# django-template

Slightly opinionated starter template for Django 1.10+ projects.

## Opinions

 - Applications should be in an "apps" folder beneath project folder
 - Project-specific, reusable classes and utils should be in "core" beneath project folder
 - Requirements should be broken out in base, local, prod and be in a "requirements" folder
 - Settings should be broken out in base, local, prod and be in a "settings" folder
 - Templates should live in a "templates" folder, not in app folders - unless the app is designed to be distributed and reusable
 - django-extensions and django-suit are awesome and are included by default

## Usage

To create a new django project with this template:

```
django-admin.py startproject --template=https://github.com/WesleyJohnson/django-template/archive/latest.zip --extension=py,gitignore project_name

mkvirtualenv {{ project_name }}
workon {{ project_name }}
cd /path/to/{{ project_name }}
pip install -r requirements/local.txt
python manage.py migrate
```