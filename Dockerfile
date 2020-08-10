FROM tiangolo/uwsgi-nginx:python3.8-alpine
RUN apk --update add bash mc
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
RUN mkdir /var/projects/visionlabs/test/images
COPY ./images /var/projects/visionlabs/test/images
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt