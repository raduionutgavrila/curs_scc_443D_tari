# PROIECT SCC - INFORMATII TEMPLATE WEB

Am incercat sa facem un template pentru partea de WEB ca sa aveti toti cam acelasi site.

app>lib>
- biblioteca_tari - modifica fiecare pt tara lui
- biblioteca_header - NU SE MODIFICA

static>
- pune poza cu steag: steag_tara.py

templates> - fisiere html pentru interfata grafica 
- base.html - NU SE MODIFICA
- <tara-mea>.html - doar copy paste cod si se modifica numai numele tarii
- home.html - se adauga tara fiecaruia pe  modelul din cod
- pagina.html - NU SE MODIFICA
- steag.html - NU SE MODIFICA

tests>
- fiecare isi face ce teste vrea

- tari.py - NU SE MODIFICA

## Pasi pentru incepere proiect

### pentru a face rost de template
1. git clone https://github.com/raduionutgavrila/curs_scc_443D_tari.git
2. git status
3. git checkout dev-template
4. git branch dev-nume-prenume

### initiere repo local pentru a incarca date in cloud ulterior
1. git remote add origin https://github.com/raduionutgavrila/curs_scc_443D_tari.git

### pentru a incarca date in cloud
1. git add .
2. git commit -m "<nume branch> - mesaj de commit"
3. git push


## Comenzi GIT

create: git branch <nume>
rename: git branch -m <name>

initiate git in directory: git init

to be able to create a branch you need to:

create a file
- git add . // stages the file> to be commited later
- git commit -m "message" // commit the changes made in file
- git pull // pull info from github to local (from up to down)
- git push -u origin main // push commits to the github repo (cloud) (from down to up)

connect to online repository
You only need to do this once per project.
git remote add origin (https://github.com/raduionutgavrila/curs_scc_443D_tari.git)


create a branch, while staying on the same branch: git checkout dev
create a branch and move to the new one: git checkout -b dev

git remote -v - afiseaza in ce repo vrei sa incarci fisiere

