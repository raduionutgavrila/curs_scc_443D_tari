FROM python:3.10-alpine

ENV FLASK_APP tari.py

RUN adduser -D franta

USER franta

WORKDIR /home/franta

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY templates templates
COPY static static
COPY tari.py tari.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5000

ENTRYPOINT ["./dockerstart.sh"]
