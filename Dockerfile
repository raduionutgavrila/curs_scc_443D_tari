<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
FROM python:3.10-alpine

ENV FLASK_APP tari
>>>>>>> origin/main_ghica_antonio
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
<<<<<<< HEAD
<<<<<<< HEAD
=======
FROM python:3.10-alpine

ENV FLASK_APP=tari

>>>>>>> origin/main_teodorescu_matei
=======
>>>>>>> origin/main_ghica_antonio
RUN adduser -D tari

USER tari

WORKDIR /home/tari
<<<<<<< HEAD
<<<<<<< HEAD
=======
RUN adduser -D canada

USER canada

WORKDIR /home/canada
>>>>>>> origin/main_roseanu_vlad
=======
>>>>>>> origin/main_teodorescu_matei

=======
FROM python:3.10-alpine

ENV FLASK_APP tari

# Cream un utilizator nou pentru a nu rula aplicatia ca root (securitate)
RUN adduser -D mexic

USER mexic

WORKDIR /home/mexic

# Copiem folderele si fisierele necesare pe rand
>>>>>>> origin/main_tudor_iulian
=======

>>>>>>> origin/main_ghica_antonio
COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY templates templates
COPY static static
COPY tari.py tari.py

<<<<<<< HEAD
<<<<<<< HEAD
RUN python3 -m venv .venv
<<<<<<< HEAD
<<<<<<< HEAD
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/tari/app
=======
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

#WORKDIR /home/canada/app
>>>>>>> origin/main_roseanu_vlad
=======
RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/tari/app
>>>>>>> origin/main_ghica_antonio

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
<<<<<<< HEAD
#CMD sh
<<<<<<< HEAD
=======
FROM python:3.8-slim
=======
FROM python:3.10-slim
>>>>>>> origin/main_voicu_ioan_andrei

WORKDIR /app

COPY . .

<<<<<<< HEAD
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
=======
# Cream mediul virtual in interiorul containerului si instalam dependintele
RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt


EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]
>>>>>>> origin/main_tudor_iulian
=======
FROM python:3.12-slim

WORKDIR /proiect

COPY quickrequirements.txt .

RUN pip install --no-cache-dir -r quickrequirements.txt

COPY tari.py .
COPY app ./app
COPY static ./static
COPY templates ./templates

EXPOSE 5011

CMD ["flask", "--app", "tari", "run", "--host=0.0.0.0", "--port=5011"]
>>>>>>> origin/main_serban_albert
=======
#CMD sh
>>>>>>> origin/main_ghica_antonio
=======
FROM python:3.12-slim

WORKDIR /app

# Copiem fișierul de dependințe
COPY quickrequirements.txt quickrequirements.txt
RUN pip install --no-cache-dir -r quickrequirements.txt

# Copiem restul fișierelor
COPY . .

# Setăm variabila de mediu necesară pentru Flask
ENV FLASK_APP=tari

# Portul impus de grup
EXPOSE 5011

# Comanda de pornire
CMD ["python3", "tari.py"]
>>>>>>> origin/main_ivan_luca
=======
RUN pip install --no-cache-dir -r quickrequirements.txt
RUN pip install flask

RUN chmod +x dockerstart.sh

ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["./dockerstart.sh"]
>>>>>>> origin/main_voicu_ioan_andrei
