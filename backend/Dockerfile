FROM python:3.4-alpine
COPY requirements.txt /var/code/requirements.txt
WORKDIR /var/code
EXPOSE 5000
RUN apk update
RUN apk add gcc musl-dev gmp-dev mpfr-dev mpc1-dev
RUN pip install -r requirements.txt
ADD . /var/code
EXPOSE 5000
CMD python backend_service.py
