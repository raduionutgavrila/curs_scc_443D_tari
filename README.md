# Proiect SCC - Țări

## 1. Identificator Dezvoltator
- **Nume:** Gheorghe Răzvan
- **Grupă:** 443D
- **Țară alocată:** România

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre România. Aceasta include:
- Definirea rutelor în `app/lib/biblioteca_romania.py`.
- Adăugarea datelor specifice (populație, capitală, vecini) în dicționarul de țări.
- Integrarea steagului în folderul `static/`.

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat
- [x] Rute Flask configurate
- [x] Interfață grafică (Templates HTML) actualizată

## 4. Testare
### Testare Manuală
Aplicația a fost verificată local rulând `python tari.py` și accesând `http://localhost:5011/tari/romania`.

### Testare Automatizată (Jenkins)
Am configurat un Pipeline în Jenkins care rulează automat testele la fiecare push pe branch-ul de dezvoltare. Toate testele din `app/tests/` au trecut cu succes (PASS).

**Dovada Build Jenkins:**
![Status Build Jenkins](screenshots/nume_poza_jenkins_1.png)
![Console Output Pytest](screenshots/nume_poza_jenkins_2.png)

## 5. Containerizare (Docker)
Aplicația a fost containerizată folosind o imagine de Python 3.12-slim. Containerul expune portul 5000 (sau 5011, după cum ai setat final).

**Dovezi Containerizare:**

*1. Imaginea Docker creată:*
![Docker Images](screenshots/docker_image.png)

*2. Containerul rulând activ:*
![Docker PS](screenshots/docker_ps.png)

*3. Accesare aplicație din container (Browser):*
![Browser Docker](screenshots/browser_docker.png)

*4. Log-uri consolă (interacțiune browser-container):*
![Docker Logs](screenshots/docker_logs.png)

## 6. Integrare și Review
- **Branch dezvoltare:** `dev_gheorghe_razvan`
- **Pull Request (PR) către main personal:** Creat, atașat screenshot-uri teste.
- **Review-uri:**
    - Am făcut review pentru colegul: [Nume Coleg / ID PR]
    - Am primit review de la: [Nume Coleg / ID PR]

## 7. Ce mai este de făcut
- [ ] Integrarea finală în branch-ul `main` al grupei după aprobarea tuturor review-urilor.