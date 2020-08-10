FROM tiangolo/uwsgi-nginx:python3.8-alpine
RUN apk --update add bash mc
RUN mkdir /var/projects/visionlabs/test
WORKDIR /var/projects/visionlabs/test
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt