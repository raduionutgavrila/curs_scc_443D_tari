FROM python:3.12-slim

WORKDIR /app

# Copiem fișierul de dependințe
COPY quickrequirements.txt quickrequirements.txt
RUN pip install --no-cache-dir -r quickrequirements.txt

# Copiem restul fișierelor
COPY . .

# Setăm variabila de mediu necesară pentru Flask
ENV FLASK_APP=tari

# Portul impus de grup
EXPOSE 5011

# Comanda de pornire
CMD ["python3", "tari.py"]
