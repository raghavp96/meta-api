## meta-api

meta-api is an API that I will be using for varying purposes, e.g. an endpoint that I can use for any Slack apps that I create, content for a website that I might build, etc. Because I'll be using it for perhaps many different things, it's sort of an API for other more single-purpose APIs. It (will be) hosted on Heroku

### Background

A little backstory:

### Notes to Self

- Ensure local Mongo instance is up and running on port 27017 (If I want to test groupy slack app features locally)

- Run with Makefile:
    - `make run`
    

- Run with gunicorn:
    - `gunicorn wsgi`

- Run in Conda Environment (Should never need to do this)
    - `conda activate slack_app_env`
    - `python app.py`

