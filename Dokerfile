FROM tiangolo/uwsgi-nginx:python3.8
RUN apk --update add bash mc
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt