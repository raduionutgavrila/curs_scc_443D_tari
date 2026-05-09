FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r quickrequirements.txt

RUN chmod +x dockerstart.sh

EXPOSE 5011

CMD ["./dockerstart.sh"]
