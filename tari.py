from flask import Flask
from app.lib.biblioteca_tari import detalii_scotia, capitala_scotia

app = Flask(__name__)

# Ruta 1: Pentru tema principală a grupei
@app.route('/')
def tema_tari():
    return "<h1>Proiect: Tema Țări - Grupa 443D</h1>"

# Ruta 2: Pentru elementul ales de tine (Scoția)
@app.route('/scotia')
def element_scotia():
    return "<h2>Bine ai venit în secțiunea dedicată Scoției!</h2>"

# Ruta 3: Pentru prima informație specifică (descriere)
@app.route('/scotia/detalii')
def ruta_detalii():
    return detalii_scotia()

# Ruta 4: Pentru a doua informație specifică (capitala)
@app.route('/scotia/capitala')
def ruta_capitala():
    return capitala_scotia()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
