FROM tiangolo/uwsgi-nginx:python3.8-alpine
RUN apk --update add bash mc
RUN mkdir -p /var/projects/visionlabs/images
RUN mkdir -p /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt