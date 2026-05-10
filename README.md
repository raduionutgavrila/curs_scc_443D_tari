# Proiect SCC - Finlanda

# 1. Dezvoltator
Nume: Mihaela Grigore
Grupă: 443D 
Țară alocată: Finlanda

# 2. Descrierea si scopul proiectului

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

# 3. Structura proiectului
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
# 4. Functionalitati implementate

In fisierul `app/lib/biblioteca_finlanda.py` au fost implementate urmatoarele functii:

## `descriere_tara()` - returneaza o descriere generala a Finlandei.

## `descriere_limbi()` - returneaza limbile oficiale vorbite in Finlanda.

## `descriere_populatie()` - returneaza populatia aproximativa a Finlandei.

## `descriere_capitala()` - returneaza capitala Finlandei.

## `descriere_steag()` - afiseaza imaginea steagului Finlandei. 

---


# 5. Rute disponibile

Aplicatia ofera urmatoarele rute web:

| Ruta | Descriere |
|---|---|
| `/finlanda` | Pagina principala pentru Finlanda |
| `/finlanda/capitala` | Afiseaza capitala Finlandei |
| `/finlanda/populatie` | Afiseaza populatia Finlandei |
| `/finlanda/limbi` | Afiseaza limbile oficiale |
| `/finlanda/steag` | Afiseaza steagul Finlandei |

---

# 6. Stadiul Implementării

- [x] Cod funcționalitate adăugat
- [x] Testare locală realizată
- [x] Containerizare Docker realizată
- [x] Pull Request creat și integrat

---

# 7. Testare

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


# 8. Containerizare Docker

Pentru containerizarea aplicației a fost creat fișierul `Dockerfile`, care îi spune Dockerului cum sa construiasca mediul in care va rula aplicatia. 

Acesta:
- utilizează imaginea `python:3.10-slim`
- copiază proiectul în container
- instalează dependențele din `quickrequirements.txt`
- pornește aplicația Flask

## Construirea imaginii Docker

Comanda utilizată:

```bash
sudo docker build -t finlanda-app .
```

Imaginea creată poate fi verificată folosind:

```bash
sudo docker images
```

## Rularea containerului

Comanda utilizată:

```bash
sudo docker run -p 5011:5011 finlanda-app
```

Aplicația a fost accesată în browser la adresa:

```text
http://127.0.0.1:5011/finlanda
```

# 9. Verificare funcționalitate

Containerul Docker rulează aplicația Flask corespunzătoare funcționalității Finlanda, iar rutele aplicației pot fi accesate din browser.

### Imagine Docker construită cu succes

Comanda utilizată:

```bash
sudo docker images
```

Rezultat:

```text
REPOSITORY     TAG           IMAGE ID       CREATED         SIZE
finlanda-app   latest        3b753abdfd24   9 minutes ago   190MB
python         3.10-slim     db7a1753878f   19 hours ago    122MB
sysinfo        v01           ba761bdd48d9   7 weeks ago     301MB
python         3.10-alpine   2deaf338e4f4   2 months ago    51.6MB
```
### Container Docker pornit

Comanda utilizată:

```bash
sudo docker run -p 5011:5011 finlanda-app
```

Rezultat:

```text
Proiect SCC - Tari
 * Serving Flask app 'tari'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5011
 * Running on http://172.17.0.2:5011
```
# 10. Integrare și Review

Branch dezvoltare:
- `dev_grigore_mihaela`

Branch principal:
- `main_grigore_mihaela`

Pull Request:
- creat
- aprobat
- merge-uit cu succes

# 11. Capturi de ecran

Capturile aferente proiectului se găsesc în directorul:

`screenshots/`
