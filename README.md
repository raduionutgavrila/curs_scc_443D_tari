# Proiect SCC - Țări

## 1. Identificator Dezvoltator
- **Nume:** Roșeanu Vlad-George
- **Grupă:** 443D
- **Țară alocată:** Canada

## 2. Funcționalitate Adăugată
Am implementat logica pentru afișarea informațiilor despre Canada. Aceasta include:
- Definirea rutelor în `app/lib/biblioteca_canada.py`.
- Adăugarea datelor specifice (populație, capitală, vecini) în dicționarul de țări.
- Integrarea steagului în folderul `static/`.

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat

## 4. Testare
### Testare Manuală
Aplicația a fost verificată local rulând `python3 tari.py` și accesând `http://localhost:5000`.

<img width="822" height="579" alt="image" src="https://github.com/user-attachments/assets/9bbce803-4a0f-4430-b57d-1c57de086974" />

<img width="1858" height="861" alt="image" src="https://github.com/user-attachments/assets/5778be5b-fd8b-49f7-862c-a38b6a4a6925" />

### Testare Automatizată (Jenkins) [ ]
Am configurat un Pipeline în Jenkins care rulează automat testele. Testul din `app/tests/` a trecut cu succes (PASS).

**Dovada Build Jenkins:**
Status Build Jenkins

<img width="1856" height="782" alt="image" src="https://github.com/user-attachments/assets/373ba633-2cb8-4047-81f2-86f3fb1ff31f" />

Console Output Pytest

<img width="1083" height="573" alt="image" src="https://github.com/user-attachments/assets/77201d1e-b950-4495-91eb-d099c0beeeab" />

## 5. Containerizare (Docker) []
Aplicația a fost containerizată folosind o imagine de Python 3.12-slim. Containerul expune portul 5011.

**Dovezi Containerizare:**

*1. Imaginea Docker creată:*
![Docker Images](screenshots/docker_images.png)

*2. Containerul rulând activ:*
![Docker PS](screenshots/docker_ps.png)

*3. Accesare aplicație din container (Browser):*
![Browser Docker](screenshots/running_browser.png)

*4. Log-uri consolă (interacțiune browser-container):*
![Docker Logs](screenshots/running_console.png)

## 6. Integrare și Review []
- **Branch dezvoltare: [Nume Coleg / ID PR]**
- **Pull Request (PR) către [Nume Coleg / ID PR]:** 
- **Review-uri:**
    - [ ] Am făcut review pentru colegul: [Nume Coleg / ID PR]
    - [ ] Am primit review de la: [Nume Coleg / ID PR]

## 7. Ce mai este de făcut
- [ ] Integrarea finală în branch-ul `main` al grupei după aprobarea tuturor review-urilor.
