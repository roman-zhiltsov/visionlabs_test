#!/bin/bash
uwsgi --socket 0.0.0.0:5000 --protocol=http -w main:app