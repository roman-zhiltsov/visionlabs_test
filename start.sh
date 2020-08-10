#!/bin/bash
app="visionlabs_test"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v /var/projects/visionlabs/test/images:/var/projects/visionlabs/test/images \
  -v $PWD:/app ${app}
