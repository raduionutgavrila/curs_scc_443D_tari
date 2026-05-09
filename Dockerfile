FROM python:3.12-slim

WORKDIR /proiect

COPY quickrequirements.txt .

RUN pip install --no-cache-dir -r quickrequirements.txt

COPY tari.py .
COPY app ./app
COPY static ./static
COPY templates ./templates

EXPOSE 5011

CMD ["flask", "--app", "tari", "run", "--host=0.0.0.0", "--port=5011"]
