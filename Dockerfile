FROM python:3.10-alpine

ENV FLASK_APP=tari

RUN adduser -D sua_user
USER sua_user
WORKDIR /home/sua_user

COPY app app
COPY templates templates
COPY static static

COPY tari.py tari.py
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY dockerstart.sh dockerstart.sh

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]