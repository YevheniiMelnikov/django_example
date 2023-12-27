FROM python:3.12.0-slim

ENV APP_HOME=/opt
ENV STATIC_ROOT=/static
ENV DJANGO_SETTINGS_MODULE=app.settings
ENV PYTHONPATH=$APP_HOME

WORKDIR $APP_HOME/
ADD requirements.txt $APP_HOME/requirements.txt
ADD app $APP_HOME/app
RUN pip install -r requirements.txt

WORKDIR $APP_HOME/app
RUN python manage.py collectstatic --no-input

EXPOSE 8000