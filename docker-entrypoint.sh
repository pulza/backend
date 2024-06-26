#!/bin/sh

echo "도커 VPC의 3306번 포트가 열릴 때까지 대기합니다."
dockerize -wait tcp://db:5432 -timeout 20s
echo "도커 VPC의 3306번 포트가 열렸습니다."
python3 manage.py runserver 0.0.0.0:8000
