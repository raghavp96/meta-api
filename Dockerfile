FROM python:3.6-alpine

# Env Vars in the Docker instance
ENV ON_HEROKU 1
ENV PORT 8080

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY *.py /
ADD slack/ slack/

RUN ls -la
RUN ls slack/apps/groupy

ENTRYPOINT ["gunicorn", "wsgi"]