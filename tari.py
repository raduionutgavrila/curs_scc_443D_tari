from flask import Flask, render_template
from app.lib.biblioteca_tari import TARI, BIBLIOTECI
from app.lib import biblioteca_header as header

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', tari=TARI)

@app.route('/danemarca')
def danemarca_home():
    tara = BIBLIOTECI['danemarca']
    return render_template('tara.html', 
                           tara_nume="Danemarca", 
                           tara="danemarca", 
                           descriere=tara.descriere_tara(), 
                           tara_url="/danemarca")

@app.route('/danemarca/capitala')
def feature_capitala():
    tara = BIBLIOTECI['danemarca']
    return render_template('pagina.html', 
                           tara_nume="Danemarca", 
                           titlu=header.header_capitala(), 
                           continut=tara.descriere_capitala(), 
                           tara_url="/danemarca")

@app.route('/danemarca/steag')
def feature_steag():
    tara = BIBLIOTECI['danemarca']
    return render_template('steag.html', 
                           header=header.header_steag(), 
                           continut=tara.descriere_steag(), 
                           tara_url="/danemarca")

@app.route('/danemarca/populatie')
def feature_populatie():
    tara = BIBLIOTECI['danemarca']
    return render_template('pagina.html', 
                           tara_nume="Danemarca", 
                           titlu=header.header_populatie(), 
                           continut=tara.descriere_populatie(), 
                           tara_url="/danemarca")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011)
