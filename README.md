# Proiect SCC - Țări

## 1. Identificator Dezvoltator
- **Nume:** Toacă Cristiana
- **Grupă:** 443D
- **Țară alocată:** Coreea de Sud

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre Coreea de Sud. Aceasta include:

- **descriere_tara()** – Returnează o descriere generală a Canadei
- **descriere_capitala()** – Returnează capitala Coreei de Sud
- **descriere_populatie()** – Returnează populația Coreei de Sud
- **descriere_limbi()** – Returnează limbile oficiale ale Coreei de Sud
- **descriere_steag()** – Returnează imaginea steagului Coreei de Sud

### Rute accesibile

| Ruta | Descriere |
|------|-----------|
| `/` | Pagina principală – lista tuturor țărilor |
| `/coreea` | Informații generale despre Coreea de Sud |
| `/coreea/capitala` | Capitala Coreei de Sud |
| `/coreea/populatie` | Populația Coreea de Sud |
| `/coreea/steag` | Steagul Coreei de Sud |

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat

## 4. Testare
### Testare Manuală
Aplicația a fost verificată local rulând `.\ruleaza_aplicatia` și accesând `http://127.0.0.1:5011/`.

**Output Consola Locala:**

![Console Output Start App](screenshots/coreea-terminal-local.png)

**Aplicatia Accesata la `http://127.0.0.1:5011/`:**

![Test local](screenshots/coreea-local.png)

### Testare Locala Folosind Pytest
Mai intai am verificat ca testele functioneaza local.

**Testare Locala cu Pytest:**

![Console Output Pytest](screenshots/coreea-teste.png)


### Testare Automata folosind Jenkins

Am configurat un Pipeline în Jenkins care rulează automat testele. Testul din `app/tests/` a trecut cu succes (PASS).

**Dovada Build Jenkins:**

![Status Build Jenkins](screenshots/coreea-jenkins.png)

**Dovada Teste Pytest in Jenkins:**

![Output Tests Jenkins](screenshots/coreea-jenkins-teste.png)

## 5. Containerizare (Docker)
Aplicația a fost containerizată folosind o imagine de Python 3.10-alpine. Containerul expune portul 5011 si poate fi accesat la `http://172.17.0.2:5011/`.

**Dovezi Containerizare:**

*1. Creare imagine Docker:*

![Docker build](screenshots/coreea-docker-build.jpeg)

*2. Start container creat:*

![Docker run](screenshots/coreea-docker-run.png)

*3. Verificare a rularii containerului:*

![Docker ps](screenshots/coreea-docker-ps.png)

*4. Accesare aplicație din container (Browser):*

Aplicatia va putea fi accesata la: `http://172.17.0.2:5011/`

![Browser-Docker](screenshots/coreea-docker-page.png)

*5. Log-uri consolă (interacțiune browser-container):*

![Docker Logs](screenshots/coreea-docker-interaction.png)

## 6. Integrare și Review
- **Branch dezvoltare: `dev_toaca_cristiana`**
- **Pull Request (PR) către `main_toaca_cristiana`:** 

## 7. Review-uri:

- [ ] Am făcut review pentru colegul: [Nume Coleg (username github) / ID PR]
- [x] Am primit review de la: [ Gavrila Radu (raduionutgavrila) / #20]

## 8. De facut
 - [x] Finalizare cod și teste manuale.
 - [x] Aplicație containerizată și accesibilă.
 - [x] Succes Pipeline Jenkins.
 - [ ] Obținerea aprobării de la colegi pentru PR-ul final, in main.
 - [ ] Integrarea finală în branch-ul main.
