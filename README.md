# Basic Django App

Because we want to actually have this all running against Django, we are going to setup a basic Django app to try things out
with.

## Setup
Install Django
```
pip install Django>=1.11.0,<2.0
```
> Note, I'm pointing at the LTS Django at the time I wrote this. Change it if you want. Maybe one day there will be good typing 
> support built in.

I did some things in the django app to get it running, so you should be able to see that now. A simple app with a single page that loads
a gif from an endpoint that changes each time the page reloads.

## Run MyPy Over It
Now lets try running mypy over this code and see what happens. Run this from the parent folder.
```
mypy typing_tutorial/
```
You should get a bunch of errors here about no stubs, something like
```
typing_training/cat_gifs/admin.py:1: error: No library stub file for module 'django.contrib'
typing_training/cat_gifs/admin.py:1: note: (Stub files are from https://github.com/python/typeshed)
typing_training/cat_gifs/apps.py:1: error: No library stub file for module 'django.apps'
typing_training/cat_gifs/models.py:1: error: No library stub file for module 'django.db'
typing_training/cat_gifs/tests.py:1: error: No library stub file for module 'django.test'
typing_training/cat_gifs/views.py:1: error: No library stub file for module 'django.views.generic'
typing_training/typing_training/urls.py:16: error: No library stub file for module 'django.conf.urls'
typing_training/typing_training/urls.py:17: error: No library stub file for module 'django.contrib'
typing_training/typing_training/wsgi.py:12: error: No library stub file for module 'django.core.wsgi'
typing_training/manage.py:8: error: No library stub file for module 'django.core.management'
typing_training/manage.py:14: error: No library stub file for module 'django'
typing_training/typing_training/settings.py:28: error: Need type annotation for variable
```
This is telling us that mypy doesn't know how to type check these modules. Django doesn't have type hints built in yet, so this makes a bit of sense.
But we want to actually do type checking in a django and not be told its all crap. So lets look at what we can do.

## Ignore Things
So the simple thing that we can do is ignore imports that do not have typing. If you run mypy as follows you will no longer see a bunch of those errors
```
mypy typing_training --ignore-missing-imports
```
This will leave you with very few errors, possibly none, that are things that are under your control. Then you can go ahead and start typing your code.

## Django Stubs
Though the core project is not typed yet, there is an attempt that someone has made to create type stubs for Django. Type stubs are seperate files that
define typing information for python files. So can we use these to help us with typing our code?

First, lets get the stubs and get them running
```
git clone git@github.com:suutari/mypy-django.git stubs
```
Now if you run the following command, you should see no errors again. What do?
```
mypy typing_training --ignore-missing-imports --strict-optional
```
Now we are actually using a bunch of typing on Django provided by the nice ppl of the internet. Yay! This wont work for parts of django-rest-framework,
but should cover some of the things that we care about.

## Typing Things in Django
So lets look at actually typing something in Django. Currently there is a simple view in cat_gifs/views. We are going to make that better by typing it.
I wouldn't actually recommend this in the real world, because you don't need to define these methods, but hey, tutorials.

Make the CatGifsView look like this
```python
class CatGifView(TemplateView):
    template_name = "gifs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Jims Finest Cat Gifs"
        })
        return context

    def get(self, request: str, *args, **kwargs) -> http.HttpResponse:
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context=context)
```
This doesn't do much, but if you run mypy now you will get a new error
```
typing_training/cat_gifs/views.py:16: error: Argument 1 of "get" incompatible with supertype "TemplateView"
```
Basically, request shouldn't be a string, because that will break prior contracts that we have established. So this is helping me find bad things in code.