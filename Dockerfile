FROM tiangolo/uwsgi-nginx:python3.8-alpine
RUN apk --update add bash mc
RUN mkdir -p /var/projects/visionlabs/test/images
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt