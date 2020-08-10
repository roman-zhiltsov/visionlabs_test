FROM tiangolo/uwsgi-nginx:python3.8-alpine
RUN apk --update add bash mc
RUN mkdir -p /var/projects/visionlabs/test/images
RUN mkdir /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt