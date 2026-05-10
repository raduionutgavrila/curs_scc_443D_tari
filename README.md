# Proiect SCC - Danemarca

## 1. Identificator Dezvoltator
**Nume:** Ivan Luca  
**Grupă:** 443D  
**Țară alocată:** Danemarca  

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre Danemarca în aplicația web Flask.
Funcționalitatea include:
* crearea fișierelor `app/lib/biblioteca_danemarca.py`, `app/lib/biblioteca_header.py` și `app/lib/biblioteca_tari.py` conform template-ului de grup;
* modificarea fișierului `tari.py` pentru integrarea Danemarcei;
* adăugarea testelor automate în `app/tests/test_lib_danemarca.py`;
* adăugarea fișierelor `Dockerfile` și `Jenkinsfile`.

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat
- [x] Teste automate adăugate
- [x] Dockerfile adăugat
- [x] Jenkinsfile adăugat
- [x] Aplicația a fost rulată local
- [x] Testele au fost rulate local cu succes

## 4. Structura Proiectului

    .
    ├── app
    │   ├── lib
    │   │   ├── biblioteca_danemarca.py
    │   │   ├── biblioteca_header.py
    │   │   ├── biblioteca_tari.py
    │   │   └── __init__.py
    │   └── tests
    │       ├── test_lib_danemarca.py
    │       └── __init__.py    ├── screenshots
    │   ├── danemarca_1_build.jpeg
    │   ├── danemarca_2_run.jpeg
    │   ├── danemarca_3_browser.png
    │   ├── danemarca_4_ps.jpeg
    │   └── danemarca_5_test.jpeg
    │   └── danemarca_6_jenkins.png
    ├── Dockerfile
    ├── Jenkinsfile
    ├── requirements.txt
    └── tari.py

## 5. Fișiere Modificate / Adăugate

**`app/lib/biblioteca_danemarca.py`**
Conține funcțiile pentru afișarea informațiilor despre Danemarca:
* `descriere_tara()`
* `descriere_limbi()`
* `descriere_populatie()`
* `descriere_capitala()`
* `descriere_steag()`

**`app/lib/biblioteca_header.py`**
Conține funcțiile standard pentru headerele paginilor.

**`app/lib/biblioteca_tari.py`**
Conține dicționarele TARI și BIBLIOTECI necesare pentru integrarea finală.

**`tari.py`**
A fost refactorizat pentru a importa noile biblioteci și a adapta rutele aplicației Flask.

**`app/tests/test_lib_danemarca.py`**
Conține testele automate (unit tests) actualizate pentru noile funcții implementate.

## 6. Rute Disponibile
| Rută | Descriere |
| :--- | :--- |
| `/` | Pagina principală a proiectului |
| `/danemarca` | Pagina principală pentru Danemarca |
| `/danemarca/capitala` | Afișează capitala Danemarcei |
| `/danemarca/steag` | Afișează steagul Danemarcei |
| `/danemarca/populatie` | Afișează populația Danemarcei |

## 7. Testare

### Testare Manuală
Aplicația a fost verificată local rulând comanda:
`python3 tari.py`

Aplicația poate fi verificată la următoarele adrese:
* `http://127.0.0.1:5011/danemarca`
* `http://127.0.0.1:5011/danemarca/capitala`
* `http://127.0.0.1:5011/danemarca/steag`
* `http://127.0.0.1:5011/danemarca/populatie`

### Testare Automată
Testele se află în folderul `app/tests/`.
Testele au fost rulate local cu succes folosind `pytest`:
![Testare Automata](screenshots/danemarca_5_test.jpeg)

## 8. Jenkins
A fost adăugat fișierul `Jenkinsfile` pentru automatizarea procesului de CI/CD.
Pipeline-ul Jenkins include etape pentru:
* **build**: pregătirea mediului;
* **test**: rularea testelor automate cu `pytest`.

![Jenkins Success](screenshots/danemarca_6_jenkins.png)
Testarea automată cu Jenkins rulează testele din folderul: `app/tests/`

## 9. Containerizare Docker
A fost adăugat fișierul `Dockerfile` pentru containerizarea aplicației.

**Construirea imaginii Docker:**
`docker build -t danemarca-app .`
![Creare Imagine](screenshots/danemarca_1_build.jpeg)

**Rularea containerului:**
`docker run -p 5000:5000 danemarca-app`
![Rulare Container](screenshots/danemarca_2_run.jpeg)

**Accesarea aplicației din container:**
![Browser App](screenshots/danemarca_3_browser.png)

**Verificare container activ:**
`docker ps`
![Docker PS](screenshots/danemarca_4_ps.jpeg)

## 10. Integrare și Review
- [ ] Crearea Pull Request-ului din `dev_ivan_luca` către `main_ivan_luca`
- [ ] Review din partea unui coleg de grupă
- [ ] Merge în branch-ul principal de documentare al grupei

## 11. Ce mai este de făcut
- [ ] Finalizarea documentației în fișierul principal README.md al repository-ului.
- [ ] Obținerea aprobării (review) pentru Pull Request.

## 12. Concluzie
Proiectul implementează funcționalitatea pentru țara Danemarca într-o structură modulară, respectând cerințele cursului SCC. Aplicația este pregătită pentru livrare prin containerizare Docker și testare automată via Jenkins.
