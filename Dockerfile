FROM python:3.10-alpine

<<<<<<< HEAD
ENV FLASK_APP tari

#3.8 alpine
RUN adduser -D tari

USER tari

WORKDIR /home/tari
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

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
=======
RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]
>>>>>>> origin/main_esterabadeyan_hadi
