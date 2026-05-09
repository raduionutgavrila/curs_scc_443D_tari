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
