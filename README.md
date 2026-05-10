# Proiect SCC - Norvegia

## 1. Identificator Dezvoltator
- **Nume:** Enache Bogdan-Gabriel
- **Grupă:** 443D
- **Țară alocată:** Norvegia

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre Norvegia. Aceasta include:

- **descriere_tara()** – Returnează o descriere generală a Norvegiei.
- **descriere_capitala()** – Returnează capitala Norvegiei: Oslo.
- **descriere_populatie()** – Returnează populația Norvegiei.
- **descriere_limbi()** – Returnează limbile oficiale ale Norvegiei.
- **descriere_steag()** – Returnează imaginea steagului Norvegiei.

### Rute accesibile

| Rută | Descriere |
|------|-----------|
| `/` | Pagina principală – lista tuturor țărilor |
| `/norvegia` | Informații generale despre Norvegia |
| `/norvegia/capitala` | Capitala Norvegiei |
| `/norvegia/populatie` | Populația Norvegiei |
| `/norvegia/steag` | Steagul Norvegiei |

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat

## 4. Testare
### Testare Manuală
Aplicația a fost verificată local rulând `./ruleaza_aplicatia` și accesând `http://127.0.0.1:5011/`.

**Output Consolă Locală:**

![Console Output Start App](screenshots/norvegia-terminal-local.png)

**Aplicația Accesată la `http://127.0.0.1:5011/`:**

![Test local](screenshots/norvegia-local.png)

### Testare Locală folosind Pytest
Mai întâi am verificat că testele funcționează local.

**Testare Locală cu Pytest:**

![Console Output Pytest](screenshots/norvegia-teste.png)

### Testare Automată folosind Jenkins

Am configurat un Pipeline în Jenkins care rulează automat testele. Testul din `app/tests/` a trecut cu succes (PASS).

**Dovadă Build Jenkins:**

![Status Build Jenkins](screenshots/norvegia-jenkins.png)

**Dovadă Teste Pytest în Jenkins:**

![Output Tests Jenkins](screenshots/norvegia-jenkins-teste.png)

## 5. Containerizare (Docker)
Aplicația a fost containerizată folosind o imagine de Python 3.10-alpine. Containerul expune portul 5011 și poate fi accesat la `http://172.17.0.2:5011/`.

**Dovezi Containerizare:**

*1. Creare imagine Docker:*

![Docker build](screenshots/norvegia-docker-build.png)

*2. Start container creat:*

![Docker run](screenshots/norvegia-docker-run.png)

*3. Verificare a rulării containerului:*

![Docker ps](screenshots/norvegia-docker-ps.png)

*4. Accesare aplicație din container (Browser):*

Aplicația va putea fi accesată la: `http://172.17.0.2:5011/`

![Browser-Docker](screenshots/norvegia-docker-page.png)

*5. Log-uri consolă (interacțiune browser-container):*

![Docker Logs](screenshots/norvegia-docker-interaction.png)

## 6. Integrare și Review
- **Branch dezvoltare:** `dev_enache_bogdan`
- **Pull Request (PR) către:** `main_enache_bogdan` - Creat

## 7. Review-uri:

- [x] Am primit review de la: [Toacă Cristiana (cr1stiaaana) #58]

## 8. De făcut
 - [x] Finalizare cod și teste manuale.
 - [x] Aplicație containerizată și accesibilă.
 - [x] Succes Pipeline Jenkins.
 - [x] Obținerea aprobării de la colegi pentru PR-ul final, în main.
 - [x] Integrarea finală în branch-ul main.
