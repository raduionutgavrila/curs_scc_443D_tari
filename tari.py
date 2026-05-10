from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lista_tari = {
        "danemarca": {
            "nume": "Danemarca"
        }
    }
    return render_template('home.html', tari=lista_tari)

@app.route('/danemarca')
def danemarca_home():
    descriere = "Danemarca este o țară situată în Europa de Nord, recunoscută pentru calitatea ridicată a vieții, peisajele sale pitorești și cultura bicicletelor."
    return render_template('tara.html', tara_nume="Danemarca", tara="danemarca", descriere=descriere, tara_url="/danemarca")

@app.route('/danemarca/capitala')
def feature_capitala():
    return render_template('pagina.html', tara_nume="Danemarca", tara="danemarca", titlu="Capitala", continut="Capitala Danemarcei este Copenhaga.", tara_url="/danemarca")

@app.route('/danemarca/steag')
def feature_steag():
    cod_html_steag = "<img src='/static/steag_danemarca.png' alt='Steag Danemarca' style='max-width: 500px;'>"
    return render_template('steag.html', tara_url="/danemarca", header="Steagul Danemarcei", continut=cod_html_steag)

@app.route('/danemarca/populatie')
def feature_populatie():
    return render_template('pagina.html', tara_nume="Danemarca", tara="danemarca", titlu="Populație", continut="Populația Danemarcei este de aproximativ 5.9 milioane de locuitori.", tara_url="/danemarca")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
