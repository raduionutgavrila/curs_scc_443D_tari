FROM python:3.10-alpine

<<<<<<< HEAD
ENV FLASK_APP tari
=======
ENV FLASK_APP canada_app
>>>>>>> origin/dev_roseanu_vlad
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
<<<<<<< HEAD
RUN adduser -D tari

USER tari

WORKDIR /home/tari
=======
RUN adduser -D canada

USER canada

WORKDIR /home/canada
>>>>>>> origin/dev_roseanu_vlad

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
=======
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

#WORKDIR /home/canada/app
>>>>>>> origin/dev_roseanu_vlad

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
<<<<<<< HEAD
#CMD sh
=======
#CMD sh
>>>>>>> origin/dev_roseanu_vlad
