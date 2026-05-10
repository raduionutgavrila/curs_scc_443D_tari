<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
FROM python:3.10-alpine

ENV FLASK_APP tari
=======
FROM python:3.10-alpine

ENV FLASK_APP canada_app
>>>>>>> origin/main_roseanu_vlad
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
<<<<<<< HEAD
=======
FROM python:3.10-alpine

ENV FLASK_APP=tari

>>>>>>> origin/main_teodorescu_matei
RUN adduser -D tari

USER tari

WORKDIR /home/tari
<<<<<<< HEAD
=======
RUN adduser -D canada

USER canada

WORKDIR /home/canada
>>>>>>> origin/main_roseanu_vlad
=======
>>>>>>> origin/main_teodorescu_matei

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY templates templates
COPY static static
COPY tari.py tari.py

RUN python3 -m venv .venv
<<<<<<< HEAD
<<<<<<< HEAD
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/tari/app
=======
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

#WORKDIR /home/canada/app
>>>>>>> origin/main_roseanu_vlad

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh
<<<<<<< HEAD
=======
FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r quickrequirements.txt

RUN chmod +x dockerstart.sh

EXPOSE 5011

CMD ["./dockerstart.sh"]
>>>>>>> origin/main_pirjol_mara
=======
FROM python:3.10-alpine

ENV FLASK_APP=tari
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser -D appuser

WORKDIR /home/appuser/proiect

COPY quickrequirements.txt .
RUN python3 -m venv .venv && \
    .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

COPY app ./app
COPY templates ./templates
COPY static ./static
COPY tari.py .
COPY pytest.ini .
COPY dockerstart.sh .

USER appuser

EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]
>>>>>>> origin/main_tecsan_calin
=======
>>>>>>> origin/main_roseanu_vlad
=======
RUN .venv/bin/pip install -r quickrequirements.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
>>>>>>> origin/main_teodorescu_matei
