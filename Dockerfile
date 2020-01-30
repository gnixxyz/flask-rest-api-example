FROM python:3.6

RUN mkdir /var/www

WORKDIR /var/www

ADD requirements.txt /var/www/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "git+https://github.com/gnixxyz/flask-apispec.git#egg=flask-apispec"
# ADD . /var/www
# CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]