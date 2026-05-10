# curs_scc_443D_tari

# Studenti - Tara
- Balaban Razvan-Marian -	Brazilia
- Ciobanu Andrei - Japonia
- Colan Bianca - Germania
- Cucui Mihai-Catalin - Laos
- Cucui Petrut-Gabriel - Nepal
- Dumitrache Alexandru - Italia
- Enache Bogdan - Norvegia 
- Esterabadeyan Hadi - Statele Unite
- Gavrilă Radu-Ionuț - Belgia
- Ghenciu Corina - Rusia
- Gheorghe Razvan - Romania
- Ghica Antonio - Namibia 
- Grigore Mihaela -	Finlanda 
- Ivan Luca - Danemarca
- Petcu Stefan-Ciprian - Serbia
- Pîrjol Mara-Olivia - Irlanda
- Roșeanu Vlad-George - Canada
- Serban Albert - Spania
- Tecșan Călin - Elveția
- Teodorescu Matei - China
- Toaca Cristiana - Corea de Sud 
- Tudor Iulian - Mexic
- Tuturluta Costi-Giani-Fabian - Franta
- Voicu Ioan-Andrei - Scoția 
- Zidu Cristian -	Estonia

## Index Țări
1. [Belgia - Gavrilă Radu-Ionuț](#belgia---gavrilă-radu-ionuț)
2. [Coreea de Sud - Toacă Cristiana](#coreea-de-sud---toacă-cristiana)
3. [Norvegia - Enache Bogdan-Gabriel](#norvegia---enache-bogdan-gabriel)
4. [România - Gheorghe Răzvan](#românia---gheorghe-răzvan)
=======

# Belgia - Gavrilă Radu-Ionuț
[Tari Proiect](#index-țări)

## Dezvoltator
- **Nume:** Gavrilă Radu-Ionuț
- **Grupa:** 443D
- **Țară alocată:** Belgia

## Cuprins
- [Descriere generală](#descriere-generală)
- [Funcționalitate implementată](#funcționalitate-implementată)
- [Stadiu dezvoltare](#stadiu-dezvoltare)
- [Testare manuală în browser](#testare-manuală-în-browser)
- [Testare automată cu pytest](#testare-automată-cu-pytest)
- [Validare cod cu pylint](#validare-cod-cu-pylint)
- [Testare cu Docker](#testare-cu-docker)
- [DevOps CI](#devops-ci)
  - [Exemplu executie pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
- [Concluzii](#concluzii)
- [Bibliografie](#bibliografie)

## Descriere generală
[cuprins](#cuprins)

Acest proiect se înscrie în tema comună a grupei 443D, „Țări”, scopul modulului fiind dezvoltarea și integrarea unui set de funcționalități dedicate țării **Belgia**.
 
Aplicația la bază este implementată utilizând framework-ul web Flask, fiind proiectată pentru a furniza date esențiale și formatate despre țara accesata. În vederea respectării practicilor moderne de inginerie software (DevOps), soluția a fost supusă testării automate (Pytest), validată static (Pylint), containerizată prin intermediul Docker și orchestrată într-un pipeline de integrare continuă (CI/CD) folosind Jenkins.

## Funcționalitate implementată
[cuprins](#cuprins)

În acest branch am adăugat și personalizat:

- Fișierul `app/lib/biblioteca_belgia.py` cu funcțiile:
  - `descriere_capitala()` – returnează capitala Belgiei.
  - `descriere_steag()` – returnează codul HTML pentru afișarea steagului Belgiei.
  - `descriere_tara()` – oferă o descriere generală a țării.
  - `descriere_limbi()` – afișează limbile oficiale (Neerlandeza, Franceza, Germana).
  - `descriere_populatie()` – afișează numărul de locuitori.

- Integrarea în fișierul de configurare globală `app/lib/biblioteca_tari.py`:
  - Declararea țării în dicționarul global `TARI`.
  - Maparea modulului aferent în dicționarul `BIBLIOTECI`.
  - Această configurare permite fișierului principal de rutare (`tari.py`) să expună dinamic următoarele endpoint-uri pentru Belgia, respectând tiparul arhitectural al proiectului:
    - `/belgia` – pagina principală a țării.
    - `/belgia/capitala` – date despre capitală.
    - `/belgia/populatie` – date demografice.
    - `/belgia/steag` – reprezentarea grafică a drapelului.

- Fișierul `app/tests/test_lib_belgia.py` care conține testele automate pentru funcțiile definite.

## Stadiu dezvoltare
[cuprins](#cuprins)

- Funcționalitate complet implementată.
- Cod adăugat în branch-ul de lucru.
- Dockerfile și Jenkinsfile sunt funcționale, urmând pipeline-ul de CI/CD.
- Testare locală, automată și containerizată realizată cu succes.

## Testare manuală în browser
[cuprins](#cuprins)

Clonarea repository-ului si selectarea ramurii de dezvoltare pentru 'Belgia':

```bash
mkdir scc
cd scc
git clone https://github.com/raduionutgavrila/curs_scc_443D_tari.git
cd curs_scc_443D_tari
git checkout dev_gavrila_radu
```

Se activează mediul virtual și se pornește aplicația cu scripturile bash existente (din rădăcina proiectului):

```bash
. ./activeaza_venv
./ruleaza_aplicatia
```



Daca apar erori de permisiuni se introduce comada:

```bash
sudo chmod 764 ./activeaza_venv ./ruleaza_aplicatia
```

Aplicația poate fi accesată în browser la adresa:

```
http://127.0.0.1:5011/
```


<img width="810" height="335" alt="belgia_venv_rulare" src="https://github.com/user-attachments/assets/ab8f673a-b317-4cb4-a6e5-25a29ea6071d" />

De asemenea, se pot verifica următoarele rute:
- `/belgia`
- `/belgia/capitala`
- `/belgia/populatie`
- `/belgia/steag`

<img width="1840" height="882" alt="Screenshot 2026-05-10 021548" src="https://github.com/user-attachments/assets/fa3d0697-1c26-4324-9a04-f0c8eca4133f" />

## Testare automată cu `pytest`
[cuprins](#cuprins)

Testele au fost scrise în fișierul `app/tests/test_lib_belgia.py`. Cu mediul virtual activ, rularea testelor se face astfel:

```bash
pytest app/tests/test_lib_belgia.py -v
```

Toate testele au fost executate cu succes, validând corectitudinea funcțiilor definite.

<img width="1168" height="583" alt="Screenshot 2026-05-10 021757" src="https://github.com/user-attachments/assets/17455151-22a0-4825-88aa-522e283722e7" />

## Validare cod cu `pylint`
[cuprins](#cuprins)

Pentru verificarea calității codului sursă se utilizează pachetul **pylint**. Acesta analizează conformitatea codului cu standardele Python (verifică spații, convenții de numire a variabilelor, variabile neutilizate etc.).

În cadrul acestui proiect, problemele raportate de **pylint** sunt doar afișate pentru monitorizare, nu sunt considerate erori.

```bash
pylint --exit-zero app/lib/biblioteca_belgia.py
pylint --exit-zero app/tests/test_lib_belgia.py
pylint --exit-zero tari.py
```


## Testare cu Docker
[cuprins](#cuprins)

Pentru asigurarea portabilității aplicației, am creat un container Docker. Pașii efectuați au fost:

1. Construirea imaginii:
```bash
docker build -t tari:v01 .
```

<img width="1167" height="213" alt="Screenshot 2026-05-10 022129" src="https://github.com/user-attachments/assets/aa7de20c-e4c0-487e-b557-0607ecb03635" />

2. Rularea containerului:
```bash
docker run -d --name tari_belgia -p 8020:5011 tari:v01
```

<img width="1642" height="108" alt="Screenshot 2026-05-10 022241" src="https://github.com/user-attachments/assets/ee8f8018-6f90-48db-9d43-a7a13d145a5c" />

3. Accesarea aplicației în browser:
```
http://localhost:8020/
```

<img width="1387" height="697" alt="Screenshot 2026-05-10 022320" src="https://github.com/user-attachments/assets/9a682c86-3b42-401e-b354-94a3df0a751d" />


# DevOps CI



- **CI** = Continuous Integration (Integrare Continuă)

Proiectul utilizează un flux de automatizare definit în `Jenkinsfile`, care asigură validarea codului și livrarea aplicației.

## Exemplu executie pipeline Jenkins

Pentru a se putea executa cu succes ultimul pas din pipeline-ul de Jenkins (crearea și lansarea containerului Docker), este necesar ca utilizatorul `jenkins` să aibă permisiuni de rulare a comenzilor Docker fără `sudo`.

Puteti gasi pasii de configurare pe [docs.docker.com - linux-postinstall](https://docs.docker.com/engine/install/linux-postinstall/).
Daca folositi masina virtuala linux, restartati masina dupa ce faceti configuratia.

**Etapele Pipeline-ului:**
1. **Build**: Crearea mediului virtual și instalarea dependințelor.
2. **Linter**: Verificarea stilului codului cu `pylint`.
3. **Unit Tests**: Rularea testelor cu `pytest`.
4. **Deploy**: Construirea imaginii Docker și pornirea containerului pe portul **8020**.


Pentru a porni serviciul, se rulează în terminal comanda:
```bash
jenkins
```
Se creează pipeline-ul în Jenkins, care este accesat local pe portul 8080 și se conectează cu repository-ul. 
Odată creat, se verifică funcționalitatea cu **Build Now**, urmat de confirmarea execuției cu succes în Console Output (log-uri).

<img width="1837" height="700" alt="Screenshot 2026-05-10 022557" src="https://github.com/user-attachments/assets/1800920c-f1ce-489c-a94c-3e05e8ba98f9" />


<img width="1805" height="905" alt="Screenshot 2026-05-10 024553" src="https://github.com/user-attachments/assets/941312ea-310a-4b24-bf9e-be3d08010c49" />


## Concluzii
[cuprins](#cuprins)

Acest proiect atinge cu succes atât obiectivele funcționale, cât și pe cele tehnice, evidențiind următoarele aspecte:

- **Dezvoltare modulară:** Implementarea unei aplicații web folosind framework-ul Flask, integrând bune practici de inginerie software.
- **Arhitectură extensibilă:** Integrarea datelor pentru Belgia a confirmat fiabilitatea separării datelor în biblioteci individuale și agregarea lor dinamică.
- **Portabilitate:** Containerizarea prin Docker a asigurat un mediu de rulare izolată, rapidă și consistentă pe diverse platforme.
- **Automatizare (CI/CD):** Pipeline-ul configurat în Jenkins a optimizat procesul de dezvoltare prin integrare și livrare continuă.
- **Asigurarea calității:** Testarea automată cu `pytest` și analiza statică a codului cu `pylint` au garantat stabilitatea aplicației la fiecare modificare a codului sursă.

## Bibliografie
[cuprins](#cuprins)

https://github.com/crchende/sysinfo.git


# Coreea de Sud - Toacă Cristiana
[Tari Proiect](#index-țări)

## 1. Identificator Dezvoltator
- **Nume:** Toacă Cristiana
- **Grupă:** 443D
- **Țară alocată:** Coreea de Sud

## 2. Funcționalitate Adăugată

Am implementat logica pentru afișarea informațiilor despre Coreea de Sud. Aceasta include:

- **descriere_tara()** – Returnează o descriere generală a Coreei de Sud.
- **descriere_capitala()** – Returnează capitala Coreei de Sud: Seul.
- **descriere_populatie()** – Returnează populația Coreei de Sud.
- **descriere_limbi()** – Returnează limbile oficiale ale Coreei de Sud.
- **descriere_steag()** – Returnează imaginea steagului Coreei de Sud.

### Rute accesibile

| Rută | Descriere |
|------|-----------|
| `/` | Pagina principală – lista tuturor țărilor |
| `/coreea` | Informații generale despre Coreea de Sud |
| `/coreea/capitala` | Capitala Coreei de Sud |
| `/coreea/populatie` | Populația Coreei de Sud |
| `/coreea/steag` | Steagul Coreei de Sud |

## 3. Stadiul Implementării
- [x] Cod funcționalitate adăugat

## 4. Testare

### Testare Manuală
Aplicația a fost verificată local rulând `.\ruleaza_aplicatia` și accesând `http://127.0.0.1:5011/`.

**Output Consolă Locală:**

![Console Output Start App](screenshots/coreea-terminal-local.png)

**Aplicația Accesată la `http://127.0.0.1:5011/`:**

![Test local](screenshots/coreea-local.png)

### Testare Locală folosind Pytest
Mai întâi am verificat că testele funcționează local.

**Testare Locală cu Pytest:**

![Console Output Pytest](screenshots/coreea-teste.png)


### Testare Automată folosind Jenkins

Am configurat un Pipeline în Jenkins care rulează automat testele. Testul din `app/tests/` a trecut cu succes (PASS).

**Dovadă Build Jenkins:**

![Status Build Jenkins](screenshots/coreea-jenkins.png)

**Dovadă Teste Pytest în Jenkins:**

![Output Tests Jenkins](screenshots/coreea-jenkins-teste.png)

## 5. Containerizare (Docker)

Aplicația a fost containerizată folosind o imagine de Python 3.10-alpine. Containerul expune portul 5011 și poate fi accesat la `http://172.17.0.2:5011/`.

**Dovezi Containerizare:**

*1. Creare imagine Docker:*

![Docker build](screenshots/coreea-docker-build.jpeg)

*2. Start container creat:*

![Docker run](screenshots/coreea-docker-run.png)

*3. Verificare a rulării containerului:*

![Docker ps](screenshots/coreea-docker-ps.png)

*4. Accesare aplicație din container (Browser):*

Aplicația va putea fi accesată la: `http://172.17.0.2:5011/`

![Browser-Docker](screenshots/coreea-docker-page.png)

*5. Log-uri consolă (interacțiune browser-container):*

![Docker Logs](screenshots/coreea-docker-interaction.png)

## 6. Integrare și Review

- **Branch dezvoltare:** `dev_toaca_cristiana`
- **Pull Request (PR) către:** `main_toaca_cristiana` - Creat

## 7. Review-uri:

- [x] Am făcut review pentru colegul: [Tuturluță Fabian (Karther1337) / #35]
- [x] Am primit review de la: [ Gavrilă Radu (raduionutgavrila) / #20]

## 8. De făcut

 - [x] Finalizare cod și teste manuale.
 - [x] Aplicație containerizată și accesibilă.
 - [x] Succes Pipeline Jenkins.
 - [ ] Obținerea aprobării de la colegi pentru PR-ul final, în main.
 - [ ] Integrarea finală în branch-ul main.

# Norvegia - Enache Bogdan-Gabriel
[Tari Proiect](#index-țări)

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

- [ ] Am primit review de la: []

## 8. De făcut

 - [x] Finalizare cod și teste manuale.
 - [x] Aplicație containerizată și accesibilă.
 - [x] Succes Pipeline Jenkins.
 - [ ] Obținerea aprobării de la colegi pentru PR-ul final, în main.
 - [ ] Integrarea finală în branch-ul main.

=======

# România - Gheorghe Răzvan
[Tari Proiect](#index-țări)

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

## 4. Testare
### Testare Manuală
Aplicația a fost verificată local rulând `./ruleaza_aplicatia` și accesând `http://localhost:5011`.

### Testare Automatizată (Jenkins)
Am configurat un Pipeline în Jenkins care rulează automat testele. Testul din `app/tests/` a trecut cu succes (PASS).

**Dovada Build Jenkins:**
![Status Build Jenkins](screenshots/romania/tests_passed_1.png)
![Console Output Pytest](screenshots/romania/tests_passed_2.png)


## 5. Containerizare (Docker)
Aplicația a fost containerizată folosind o imagine de Python 3.12-slim. Containerul expune portul 5011.

**Dovezi Containerizare:**

*1. Imaginea Docker creată:*
![Docker Images](screenshots/romania/docker_images.png)

*2. Containerul rulând activ:*
![Docker PS](screenshots/romania/docker_ps.png)

*3. Accesare aplicație din container (Browser):*
![Browser Docker](screenshots/romania/running_browser.png)

*4. Log-uri consolă (interacțiune browser-container):*
![Docker Logs](screenshots/romania/running_console.png)

## 6. Integrare și Review
- **Branch dezvoltare: `dev_gheorghe_razvan`**
- **Pull Request (PR) către `main_gheorghe_razvan`:** 
Creat
- **Review-uri:**
    - [x] Am făcut review pentru colegul: Serban Albert / PR ID #72
    - [x] Am primit review de la: Zidu Cristian / PR ID: #6

## 7. Ce mai este de făcut
- [x] Integrarea finală în branch-ul `main` al grupei după aprobarea tuturor review-urilor.
