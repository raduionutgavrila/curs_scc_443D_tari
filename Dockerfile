FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5011

CMD ["python3", "-m", "flask", "--app", "tari", "run", "--host=0.0.0.0", "--port=5011"]
