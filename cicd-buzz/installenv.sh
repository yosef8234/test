#!/bin/sh
virtualenv venv
source venv/bin/activate
python -m pytest -v tests/test_generator.py
docker build -t cicd-buzz .
docker run -p 5000:5000 --rm -it cicd-buzz
#docker run -p5000:5000 --rm -it <YOUR_DOCKER_USERNAME>/cicd-buzz:latest