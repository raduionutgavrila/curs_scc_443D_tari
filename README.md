# Proiect SCC - Finlanda

## Student
Mihaela Grigore

## Descrierea si scopul proiectului

Scopul acestui proiect este dezvoltarea unei aplicații software colaborative în cadrul grupei de laborator, în care fiecare student implementează propria funcționalitate asociată unei țări alese.

Proiectul urmărește utilizarea unor concepte și tehnologii specifice dezvoltării moderne de aplicații software, precum:
- dezvoltarea colaborativă folosind Git și GitHub;
- gestionarea branch-urilor de dezvoltare individuale;
- integrarea modificărilor prin Pull Request-uri;
- testarea automată a funcționalităților utilizând Pytest și Jenkins;
- verificarea și analiza codului adăugat de ceilalți membri ai echipei;
- pregătirea aplicației pentru livrare și rulare în containere folosind Docker.

Tema aleasa pentru acest proiect este reprezentarea tarii Finlanda prin intermediul unor rute web care afiseaza informatii generale despre tara, populatie, limbi oficiale, capitala si steag.

Aplicatia utilizeaza:
- Python
- Flask
- Pytest
- Git/GitHub
- mediu virtual Python (venv)

---

# Structura proiectului
```text
├── activeaza_venv
├── activeaza_venv_jenkins
├── app
│   ├── lib
│   │   ├── biblioteca_finlanda.py
│   │   ├── biblioteca_header.py
│   │   ├── biblioteca_tari.py
│   │   └── __pycache__
│   │       ├── biblioteca_finlanda.cpython-310.pyc
│   │       ├── biblioteca_header.cpython-310.pyc
│   │       └── biblioteca_tari.cpython-310.pyc
│   └── tests
│       ├── __pycache__
│       │   └── test_lib_finlanda.cpython-310-pytest-9.0.3.pyc
│       └── test_lib_finlanda.py
├── dockerstart.sh
├── LICENSE
├── __pycache__
│   └── tari.cpython-310.pyc
├── pytest.ini
├── quickrequirements.txt
├── README.md
├── ruleaza_aplicatia
├── static
│   └── steag_finlanda.png
├── tari.py
└── templates
    ├── base.html
    ├── home.html
    ├── pagina.html
    ├── steag.html
    └── tara.html

```

## Directoare importante

### `app/lib/`

Contine bibliotecile Python utilizate pentru gestionarea informatiilor despre tari.

Fisiere modificate:
- `biblioteca_finlanda.py`
- `biblioteca_tari.py`

### `app/tests/`

Contine testele automate realizate cu Pytest.

Fisier adaugat:
- `test_lib_finlanda.py`

### `static/`

Contine fisiere statice utilizate de aplicatie.

Fisier adaugat:
- `steag_finlanda.png`

### `templates/`

Contine paginile HTML utilizate de Flask pentru afisarea informatiei in browser.

Aceste fisiere NU au fost modificate conform cerintei proiectului.

---

# Functionalitati implementate

In fisierul `app/lib/biblioteca_finlanda.py` au fost implementate urmatoarele functii:

## `descriere_tara()`

Returneaza o descriere generala a Finlandei.

## `descriere_limbi()`

Returneaza limbile oficiale vorbite in Finlanda.

## `descriere_populatie()`

Returneaza populatia aproximativa a Finlandei.

## `descriere_capitala()`

Returneaza capitala Finlandei.

## `descriere_steag()`

Afiseaza imaginea steagului Finlandei utilizand fisierul:
`/static/steag_finlanda.png`

---

# Configurarea bibliotecii tarii

Fisierul `app/lib/biblioteca_tari.py` a fost modificat pentru:
- importarea bibliotecii Finlandei
- adaugarea tarii in dictionarul `TARI`
- maparea bibliotecii in dictionarul `BIBLIOTECI`

Configuratia finala permite accesarea automata a rutelor pentru Finlanda din aplicatia Flask.

---

# Rute disponibile

Aplicatia ofera urmatoarele rute web:

| Ruta | Descriere |
|---|---|
| `/finlanda` | Pagina principala pentru Finlanda |
| `/finlanda/capitala` | Afiseaza capitala Finlandei |
| `/finlanda/populatie` | Afiseaza populatia Finlandei |
| `/finlanda/limbi` | Afiseaza limbile oficiale |
| `/finlanda/steag` | Afiseaza steagul Finlandei |

---

# Testare automata

Fisier de test:
- `app/tests/test_lib_finlanda.py`

## Functii testate

- `descriere_tara()`
- `descriere_populatie()`
- `descriere_capitala()`
- `descriere_limbi()`

Testele verifica daca valorile returnate de functii sunt identice cu valorile asteptate.

## Comanda utilizata pentru testare

```bash
python3 -m pytest app/tests/test_lib_finlanda.py


===================================== test session starts ======================================
platform linux -- Python 3.10.12, pytest-9.0.3, pluggy-1.6.0
rootdir: /home/miki/curs_scc_443D_tari
configfile: pytest.ini
collected 4 items                                                                              

app/tests/test_lib_finlanda.py::test_functie_descriere_tara 
---------------------------------------- live log call -----------------------------------------
2026-05-09 08:37:08 [INFO    ] (test_lib_finlanda.py:11) Merge functia descriere_tara
PASSED                                                                                   [ 25%]
app/tests/test_lib_finlanda.py::test_functie_populatie 
---------------------------------------- live log call -----------------------------------------
2026-05-09 08:37:08 [INFO    ] (test_lib_finlanda.py:18) Merge functia descriere_populatie
PASSED                                                                                   [ 50%]
app/tests/test_lib_finlanda.py::test_functie_capitala 
---------------------------------------- live log call -----------------------------------------
2026-05-09 08:37:08 [INFO    ] (test_lib_finlanda.py:25) Merge functia descriere_capitala
PASSED                                                                                   [ 75%]
app/tests/test_lib_finlanda.py::test_functie_limbi 
---------------------------------------- live log call -----------------------------------------
2026-05-09 08:37:08 [INFO    ] (test_lib_finlanda.py:32) Merge functia descriere_limbi
PASSED                                                                                   [100%]

====================================== 4 passed in 0.04s =======================================

