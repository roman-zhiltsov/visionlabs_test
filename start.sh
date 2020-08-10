#!/bin/bash
app="visionlabs_test"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/var/projects/visionlabs/test ${app}