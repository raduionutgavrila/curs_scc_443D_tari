FROM python:3.12-slim

WORKDIR /app

COPY quickrequirements.txt .

RUN pip install --no-cache-dir -r quickrequirements.txt

COPY . .

RUN chmod 764 activeaza_venv ruleaza_aplicatia dockerstart.sh

EXPOSE 5011

CMD ["./dockerstart.sh"]