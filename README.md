# Proiect SCC - Țări - Italia

## Dezvoltator
- **Nume:** Dumitrache Alexandru
- **Grupa:** 443D
- **Tema:** Țări
- **Element:** Italia
- **Branch de dezvoltare:** `dev_dumitrache_alexandru`

---

## Funcționalitate adăugată

Am adăugat funcționalitate referitoare la **Italia** în fișierul `app/lib/biblioteca_italia.py`:

- **descriere_tara()** – Returnează o descriere generală a Italiei
- **descriere_capitala()** – Returnează informații despre capitala Roma
- **descriere_populatie()** – Returnează informații despre populația Italiei
- **descriere_limbi()** – Returnează limbile oficiale ale Italiei
- **descriere_steag()** – Returnează descrierea și imaginea steagului Italiei

### Rute disponibile

| Ruta | Descriere |
|------|-----------|
| `/` | Pagina principală – lista tuturor țărilor |
| `/italia` | Informații generale despre Italia |
| `/italia/capitala` | Capitala Italiei – Roma |
| `/italia/populatie` | Populația Italiei |
| `/italia/steag` | Steagul Italiei |

### Fișiere modificate/adăugate
- `app/lib/biblioteca_italia.py` – **NOU** – biblioteca cu funcțiile pentru Italia
- `app/lib/biblioteca_tari.py` – **MODIFICAT** – adăugat import și înregistrare Italia în TARI și BIBLIOTECI
- `app/tests/test_lib_italia.py` – **NOU** – teste unitare pentru Italia
- `Jenkinsfile` – **NOU** – pipeline declarativ pentru Jenkins
- `Dockerfile` – **NOU** – containerizarea aplicației

---

## Stadiul implementării

- [x] Cod funcționalitate adăugat (`app/lib/biblioteca_italia.py`)
- [x] Italia înregistrată în `biblioteca_tari.py` (TARI + BIBLIOTECI)
- [x] Teste unitare scrise (`app/tests/test_lib_italia.py`)
- [x] Jenkinsfile configurat
- [x] Dockerfile creat
- [x] README.md completat

---

## Testare

### Testare manuală
Aplicația a fost verificată local rulând `./ruleaza_aplicatia` și accesând `http://localhost:5011`.

### Testare cu Jenkins
- Fișierul `Jenkinsfile` este configurat cu un pipeline declarativ
- Pipeline-ul conține etapele: Build, Verificare calitate cod (pylint), Teste unitare (pytest)
- Testele unitare se execută cu `pytest`
- **Rezultat:** PASS

**Dovada Build Jenkins:**
![Jenkins OK](screenshots/italia_jenkinsok.png)
![Jenkins Success](screenshots/italia_jsuccess.png)

### Teste unitare (4/4 PASS)
- `test_functie_descriere_tara` – PASS
- `test_functie_populatie` – PASS
- `test_functie_capitala` – PASS
- `test_functie_limbi` – PASS

---

## Containerizare

### Construire imagine Docker
```bash
docker build -t scc_tari_italia .
```

### Creare și rulare container
```bash
docker run -d -p 5011:5011 --name tari_italia scc_tari_italia
```

### Accesare aplicație din browser
Aplicația poate fi accesată la: `http://localhost:5011/italia`

### Capturi de ecran

*Terminal - docker images, docker ps, docker logs:*
![Docker Terminal](screenshots/italia_dockerterm.png)

*Browser - accesare aplicație din container:*
![Docker Browser](screenshots/italia_dockerbrowser.png)

---

## Integrare (Pull Request)

- Branch sursă: `dev_dumitrache_alexandru`
- Branch destinație: `main_dumitrache_alexandru`
- Status: COMPLETAT
- Review de la: `Teodorescu-Colciu Matei`

---

## Pull Request-uri la care am făcut review

| PR ID | Autor | Descriere |
|-------|-------|-----------|
| *(de completat)* | *(de completat)* | *(de completat)* |

---

## Ce mai este de făcut

- [x] Obținere review de la un coleg
- [ ] Integrare README.md în branch-ul main
- [ ] Review la PR-ul unui coleg
