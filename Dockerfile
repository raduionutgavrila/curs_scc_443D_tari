FROM python:3.10-alpine

ENV FLASK_APP canada_app
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D canada

USER canada

WORKDIR /home/canada

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY templates templates
COPY static static
COPY tari.py tari.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

#WORKDIR /home/canada/app

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh
