FROM python:3.12-slim

WORKDIR /app

COPY quickrequirements.txt .

RUN pip install --no-cache-dir -r quickrequirements.txt

COPY . .

ENV FLASK_APP=tari

EXPOSE 5011

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5011"]