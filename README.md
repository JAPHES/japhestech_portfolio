# Japhestech Portfolio (Django 5)

Personal portfolio site built with Django and deployed on Vercel using Python serverless functions plus WhiteNoise for static files.

## Stack
- Python / Django 5
- WhiteNoise for static assets
- Vercel serverless runtime (`@vercel/python`)

## Local Development
1) Create and activate a virtualenv.  
2) Install deps: `pip install -r requirements.txt`  
3) Run migrations (none needed for the static site, but Django expects a DB): `python manage.py migrate`  
4) Start dev server: `python manage.py runserver`  
   - Static files are served by Django in debug.

## Deployment (Vercel)
- Build: `pip install -r requirements.txt`  
- Collect static: `python manage.py collectstatic --noinput --clear`  
- Serverless entrypoint: `api/index.py` (WSGI wrapped with WhiteNoise)  
- Routes: all requests go to `api/index.py` (WhiteNoise serves `/static/` from `staticfiles`).  
- Required env vars:
  - `DJANGO_SETTINGS_MODULE=japhestech.settings`
  - `SECRET_KEY=your-secret-key`
  - `DEBUG=False`
  - `VERCEL_URL=japhestec.vercel.app`

## Live Site
https://japhestec.vercel.app/
