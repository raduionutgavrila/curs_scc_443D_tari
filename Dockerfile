FROM python:3.10-alpine

ENV FLASK_APP tari

# Cream un utilizator nou pentru a nu rula aplicatia ca root (securitate)
RUN adduser -D mexic

USER mexic

WORKDIR /home/mexic

# Copiem folderele si fisierele necesare pe rand
COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY templates templates
COPY static static
COPY tari.py tari.py

# Cream mediul virtual in interiorul containerului si instalam dependintele
RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt


EXPOSE 5011

ENTRYPOINT ["./dockerstart.sh"]