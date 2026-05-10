# Proiect SCC - Scoția

## 1. Identificator Dezvoltator
* **Nume:** Voicu Ioan-Andrei
* **Grupă:** 443D
* **Țară alocată:** Scoția

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre Scoția în aplicația web Flask.
Funcționalitatea include:
* crearea fișierului `app/lib/scotia.py`;
* modificarea fișierului `tari.py` pentru integrarea Scoției;
* adăugarea testelor automate în `app/tests/test_lib_scotia.py`;
* adăugarea fișierelor `Dockerfile` și `Jenkinsfile`.

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat
- [x] Teste automate adăugate
- [x] Dockerfile adăugat
- [x] Jenkinsfile adăugat
- [x] Aplicația a fost rulată local
- [x] Testele au fost rulate local cu succes

## 4. Structura Proiectului
```text
.
├── app
│   ├── lib
│   │   ├── scotia.py
│   │   └── __init__.py
│   ├── tests
│   │   └── test_lib_scotia.py
│   └── __init__.py
├── screenshots
│   ├── scotia-teste.png
│   ├── scotia-terminal-local.png
│   ├── scotia-local.png
│   ├── scotia-jenkins.png
│   ├── scotia-jenkins-teste.png
│   ├── scotia-docker-build.png
│   ├── scotia-docker-run.png
│   ├── scotia-docker-ps.png
│   └── scotia-docker-page.png
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── quickrequirements.txt
└── tari.py
## 5. Fișiere Modificate / Adăugate
**`app/lib/scotia.py`**
Conține funcțiile pentru afișarea informațiilor despre Scoția:
* `descriere_tara()`
* `capitala_tara()`
* `steag_tara()`
* `populatie_tara()`

**`tari.py`**
A fost modificat pentru:
* importarea bibliotecii Scoției;
* definirea rutelor specifice în aplicația Flask.

**`app/tests/test_lib_scotia.py`**
Conține testele automate (unit tests) pentru funcțiile implementate în bibliotecă (capitală, limbi, populație, steag, țară).

## 6. Rute Disponibile
| Rută | Descriere |
|---|---|
| `/` | Pagina principală a proiectului |
| `/scotia` | Pagina principală pentru Scoția |
| `/scotia/capitala` | Afișează capitala Scoției |
| `/scotia/steag` | Afișează steagul Scoției |
| `/scotia/populatie` | Afișează populația Scoției |

## 7. Testare
**Testare Manuală**
Aplicația a fost verificată local activând mediul virtual și rulând scriptul:
```bash
. ./activeaza_venv
./ruleaza_aplicatia
Aplicația a fost accesată în browser la adresa: http://127.0.0.1:5011

Testare Automată
Testele se află în folderul app/tests/.
Testele au fost rulate local cu succes (100% Passed) folosind comanda:
python3 -m pytest app/tests/test_lib_scotia.py -v

##8. Jenkins

A fost adăugat/modificat fișierul Jenkinsfile pentru automatizarea procesului de CI/CD.
Pipeline-ul Jenkins include etape pentru:

    build: pregătirea mediului;

    test: rularea testelor automate cu comanda python3.
    Testarea automată cu Jenkins rulează testele din locația: app/tests/test_lib_scotia.py

##9. Containerizare Docker

A fost adăugat fișierul Dockerfile pentru containerizarea aplicației (folosind imaginea de bază python:3.10-slim).
Construirea imaginii Docker:
sudo docker build -t proiect-scotia .
Rularea containerului (pe portul 5011):
sudo docker run -d -p 5011:5011 --name scotia-app proiect-scotia
Accesarea aplicației din container s-a făcut din browser la adresa: http://127.0.0.1:5011/scotia