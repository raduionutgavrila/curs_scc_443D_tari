FROM python:3.10-alpine

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
ENV FLASK_APP tari
=======
ENV FLASK_APP tari
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site
>>>>>>> origin/main_zidu_cristian

#3.8 alpine
RUN adduser -D tari

USER tari

WORKDIR /home/tari
<<<<<<< HEAD
=======
ENV FLASK_APP=tari

RUN adduser -D sua_user
USER sua_user
WORKDIR /home/sua_user
>>>>>>> origin/main_esterabadeyan_hadi

COPY app app
COPY templates templates
COPY static static

COPY tari.py tari.py
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY dockerstart.sh dockerstart.sh

<<<<<<< HEAD
#RUN mkdir static
#RUN mkdir static/imagini
#RUN chmod -R 777 static

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt
=======
=======
ENV FLASK_APP tari.py

RUN adduser -D franta

USER franta

WORKDIR /home/franta
>>>>>>> origin/main_tuturluta_fabian

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY templates templates
COPY static static
COPY tari.py tari.py

RUN python3 -m venv .venv
<<<<<<< HEAD
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/tari/app
>>>>>>> origin/main_zidu_cristian

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
<<<<<<< HEAD
=======
RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]
>>>>>>> origin/main_esterabadeyan_hadi
=======
#CMD sh
>>>>>>> origin/main_zidu_cristian
=======
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5000

ENTRYPOINT ["./dockerstart.sh"]
>>>>>>> origin/main_tuturluta_fabian
