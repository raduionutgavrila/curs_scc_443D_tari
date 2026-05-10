# Proiect SCC - Țări

## 1. Identificator Dezvoltator
- **Nume:** Serban Albert
- **Grupă:** 443D
- **Țară alocată:** Spania

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre Spania. Aceasta include:
- Definirea rutelor în `app/lib/biblioteca_spania.py`.
- Adăugarea datelor specifice (populație, capitală, vecini) în dicționarul de țări.
- Integrarea steagului în folderul `static/`.

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat

## 4. Testare
### Testare Manuală
Aplicația a fost verificată local rulând `./ruleaza_aplicatia` și accesând `http://localhost:5011`.

### Testare Automatizată (Jenkins)
Am configurat un Pipeline în Jenkins care rulează automat testele. Testul din `app/tests/` a trecut cu succes (PASS).

**Dovada Build Jenkins:**
![Status Build Jenkins](screenshots/spania_tests_passed_1.png)
![Console Output Pytest](screenshots/spania_tests_passed_2.png)

## 5. Containerizare (Docker)
Aplicația a fost containerizată folosind o imagine de Python 3.12-slim. Containerul expune portul 5011.

**Dovezi Containerizare:**

*1. Imaginea Docker creată:*
![Docker Images](screenshots/spania_docker_images.png)

*2. Containerul rulând activ:*
![Docker PS](screenshots/spania_docker_ps.png)

*3. Accesare aplicație din container (Browser):*
![Browser Docker](screenshots/spania_running_browser.png)

*4. Log-uri consolă (interacțiune browser-container):*
![Docker Logs](screenshots/spania_running_console.png)

## 6. Integrare și Review
- **Branch dezvoltare: `dev_serban_albert`**
- **Pull Request (PR) către `main_serban_albert`:** 
Creat
- **Review-uri:**
    - [ ] Am făcut review pentru colegul: [Nume Coleg / ID PR]
    - [x] Am primit review de la: Zidu Cristian / PR ID: #6

## 7. Ce mai este de făcut
- [ ] Integrarea finală în branch-ul `main` al grupei după aprobarea tuturor review-urilor.
