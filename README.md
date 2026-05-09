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
- `test/test_italia.py` – **NOU** – teste unitare pentru Italia
- `Jenkinsfile` – **NOU** – pipeline declarativ pentru Jenkins
- `Dockerfile` – **NOU** – containerizarea aplicației

---

## Stadiul implementării

- [x] Cod funcționalitate adăugat (`app/lib/biblioteca_italia.py`)
- [x] Italia înregistrată în `biblioteca_tari.py` (TARI + BIBLIOTECI)
- [x] Teste unitare scrise (`test/test_italia.py`)
- [x] Jenkinsfile configurat
- [x] Dockerfile creat
- [x] README.md completat

---

## Testare

### Testare manuală
Aplicația a fost testată manual prin rularea:
```bash
python tari.py
```
Apoi s-a accesat fiecare rută din browser la adresa `http://localhost:5000`.

### Testare cu Jenkins
- Fișierul `Jenkinsfile` este configurat cu un pipeline declarativ
- Pipeline-ul conține etapele: Clone, Install Dependencies, Test
- Testele unitare se execută cu `pytest`
- **Rezultat:** PASS

### Teste unitare (17/17 PASS)
- `test_descriere_tara_returneaza_string` – PASS
- `test_descriere_tara_contine_italia` – PASS
- `test_descriere_tara_nu_e_gol` – PASS
- `test_descriere_capitala_returneaza_string` – PASS
- `test_descriere_capitala_contine_roma` – PASS
- `test_descriere_populatie_returneaza_string` – PASS
- `test_descriere_populatie_contine_milioane` – PASS
- `test_descriere_steag_returneaza_string` – PASS
- `test_descriere_steag_contine_tricolor` – PASS
- `test_ruta_index` – PASS
- `test_ruta_index_contine_italia` – PASS
- `test_ruta_italia` – PASS
- `test_ruta_italia_capitala` – PASS
- `test_ruta_italia_populatie` – PASS
- `test_ruta_italia_steag` – PASS
- `test_ruta_capitala_contine_roma` – PASS
- `test_ruta_inexistenta_404` – PASS

---

## Containerizare

### Construire imagine Docker
```bash
docker build -t scc_tari_italia .
```

### Creare și rulare container
```bash
docker run -d -p 5000:5000 --name tari_italia scc_tari_italia
```

### Accesare aplicație din browser
Aplicația poate fi accesată la: `http://localhost:5000/italia`

### Capturi de ecran
*(Adăugați aici capturile de ecran conform cerințelor:)*
- [ ] Imaginea de container creată (`docker images`)
- [ ] Containerul creat (`docker ps`)
- [ ] Browserul accesând aplicația
- [ ] Mesajele din consolă care atestă accesarea aplicației

---

## Integrare (Pull Request)

- Branch sursă: `dev_dumitrache_alexandru`
- Branch destinație: `main_dumitrache_alexandru`
- Status: *(de completat)*
- Review de la: *(de completat cu numele colegului)*

---

## Pull Request-uri la care am făcut review

| PR ID | Autor | Descriere |
|-------|-------|-----------|
| *(de completat)* | *(de completat)* | *(de completat)* |

---

## Ce mai este de făcut

- [ ] Adăugare capturi de ecran containerizare
- [ ] Obținere review de la un coleg
- [ ] Integrare README.md în branch-ul main
- [ ] Review la PR-ul unui coleg
