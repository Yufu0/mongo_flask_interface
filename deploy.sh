#!/bin/bash

docker build -t myapp:latest .

docker run -d -p 80:80 myapp:latest
