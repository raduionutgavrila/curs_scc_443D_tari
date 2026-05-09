from flask import Flask
from app.lib.danemarca import descriere_danemarca, capitala_danemarca

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Proiect: Tari (Grupa 443D)</h1><p>Alege o tara din URL, de ex: /danemarca</p>"

@app.route('/danemarca')
def danemarca_home():
    return "<h2>Informatii despre Danemarca</h2><p>Acceseaza /danemarca/descriere sau /danemarca/capitala</p>"

@app.route('/danemarca/descriere')
def feature_descriere():
    return descriere_danemarca()

@app.route('/danemarca/capitala')
def feature_capitala():
    return capitala_danemarca()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
