FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r quickrequirements.txt
RUN pip install flask

RUN chmod +x dockerstart.sh

ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["./dockerstart.sh"]