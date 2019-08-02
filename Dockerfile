FROM python:3.6-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY *.py /
ADD slack/ slack/

RUN ls -la

# Env Vars in the Docker instance
ENV ON_HEROKU 1
ENV PORT 8080

ENTRYPOINT ["gunicorn", "wsgi"]