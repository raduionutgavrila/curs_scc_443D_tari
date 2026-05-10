FROM python:3.10-alpine

ENV FLASK_APP sysinfo

#3.8 alpine
RUN adduser -D nvg_user

USER nvg_user

WORKDIR /home/nvg_user

COPY app app
COPY templates templates
COPY static static

COPY tari.py tari.py
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY dockerstart.sh dockerstart.sh

#RUN mkdir static
#RUN mkdir static/imagini
#RUN chmod -R 777 static

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
