# Proiect SCC - Rusia

## 1. Identificator Dezvoltator

**Nume:** Corina Ghenciu  
**Grupă:** 443D  
**Țară alocată:** Rusia  

---

## 2. Funcționalitate Adăugată

Am implementat logica pentru afișarea informațiilor despre Rusia în aplicația web Flask.

Funcționalitatea include:

- crearea fișierului `app/lib/biblioteca_rusia.py`;
- modificarea fișierului `app/lib/biblioteca_tari.py` pentru integrarea Rusiei în aplicație;
- adăugarea testelor automate în `app/tests/test_lib_rusia.py`;
- adăugarea steagului Rusiei în folderul `static/`;
- adăugarea fișierelor `Dockerfile` și `Jenkinsfile`.

Descrierea Rusiei include informații generale despre țară, capitală, cultură, atracții istorice și peisaje naturale importante.

Au fost incluse atracții precum:

- Kremlinul din Moscova;
- Piața Roșie;
- Muzeul Ermitaj din Sankt Petersburg;
- Lacul Baikal.

---

## 3. Stadiul Implementării

- [x] Cod funcționalitate adăugat
- [x] Teste automate adăugate
- [x] Steag Rusia adăugat
- [x] Dockerfile adăugat
- [x] Jenkinsfile adăugat
- [x] Aplicația a fost rulată local
- [x] Testele au fost rulate local cu succes
- [x] Aplicația a fost rulată în container Docker
- [ ] Pipeline-ul Jenkins a fost rulat cu succes

---

## 4. Structura Proiectului

```text
.
├── activeaza_venv
├── activeaza_venv_jenkins
├── app
│   ├── lib
│   │   ├── biblioteca_rusia.py
│   │   ├── biblioteca_header.py
│   │   └── biblioteca_tari.py
│   └── tests
│       └── test_lib_rusia.py
├── dockerstart.sh
├── Dockerfile
├── Jenkinsfile
├── pytest.ini
├── quickrequirements.txt
├── README.md
├── ruleaza_aplicatia
├── screenshots
│   ├── rusia_docker_browser.png
│   ├── rusia_docker_build.png
│   ├── rusia_jenkins_build_pass.png
│   ├── rusia_jenkins_console_output.png
│   └── rusia_pytest.png
├── static
│   └── steag_rusia.png
├── tari.py
└── templates
    ├── base.html
    ├── home.html
    ├── pagina.html
    ├── steag.html
    └── tara.html
