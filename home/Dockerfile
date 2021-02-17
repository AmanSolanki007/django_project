FROM python:3

WORKDIR /usr/django_app

COPY ./ ./ 

RUN pip3 install -r requirements.txt

CMD ["python manage.py runserver"]