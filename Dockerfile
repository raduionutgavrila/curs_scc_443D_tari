FROM python:3.10-alpine

ENV FLASK_APP=tari.py

RUN adduser -D razvan

WORKDIR /home/razvan/

COPY app app
COPY static static
COPY templates templates
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY tari.py tari.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

RUN chown -R razvan:razvan /home/razvan

USER razvan

EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]
