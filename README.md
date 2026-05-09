# Proiect SCC - Țări

## 1. Identificator Dezvoltator
- **Nume:** Toacă Cristiana
- **Grupă:** 443D
- **Țară alocată:** Coreea de Sud

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre Coreea de Sud. Aceasta include:
- Definirea rutelor în `app/lib/biblioteca_coreea.py`.
- Adăugarea datelor specifice (descrierea tarii, limbi vorbite, populație, capitală) în dicționarul, `biblioteca_coreea` de țări.
- Integrarea steagului în folderul `static/`.

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat

## 4. Testare
### Testare Manuală
Aplicația a fost verificată local rulând `.\ruleaza_aplicatia` și accesând `http://127.0.0.1:5011/`.

![Test local](screenshots/ss-local.png)

### Testare folosind Pytest
Mai intai am verificat ca testele functioneaza local.

**Testare locala cu pytest:**
![Console Output Pytest](screenshots/ss-teste.png)


### Testare Automata folosind Jenkins

Am configurat un Pipeline în Jenkins care rulează automat testele. Testul din `app/tests/` a trecut cu succes (PASS).
**Dovada Build Jenkins:**
![Status Build Jenkins](screenshots/tests_passed_1.png)

## 5. Containerizare (Docker)
Aplicația a fost containerizată folosind o imagine de Python 3.10-alpine. Containerul expune portul 5011 si poate fi accesat la `http://172.17.0.2:5011/`.

**Dovezi Containerizare:**

*1. Creare imagine Docker:*

![Docker build](screenshots/ss-docker-build.jpeg)

*2. Start container creat:*

![Docker run](screenshots/ss-docker-run.png)

*3. Verificare a rularii containerului:*

![Docker ps](screenshots/ss-docker-ps.png)

*4. Accesare aplicație din container (Browser):*

Aplicatia va putea fi accesata la: `http://172.17.0.2:5011/`
![Browser-Docker](screenshots/ss-docker-page.png)

*5. Log-uri consolă (interacțiune browser-container):*

![Docker Logs](screenshots/ss-docker-interaction.png)

## 6. Integrare și Review
- **Branch dezvoltare: `dev_toaca_cristiana`**
- **Pull Request (PR) către `main_toaca_cristiana`:** 

## 7. Ce mai este de făcut
- [ ] Integrarea finală în branch-ul `main` al grupei după aprobarea tuturor review-urilor.