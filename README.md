# PROIECT SCC - INFORMATII TEMPLATE WEB

Am incercat sa facem un template pentru partea de WEB ca sa aveti toti cam acelasi site.

app>lib>
- `biblioteca_tara` - modifica fiecare pt tara lui
- `biblioteca_header` - NU SE MODIFICA

static>
- `pune poza cu steag` - steag_tara.py

templates> - fisiere html pentru interfata grafica 
- `base.html` - NU SE MODIFICA
- `<tara-mea>.html` - doar copy paste cod si se modifica numai numele tarii
- `home.html` - se adauga tara fiecaruia pe  modelul din cod
- `pagina.html` - NU SE MODIFICA
- `steag.html` - NU SE MODIFICA

tests>
- fiecare isi face ce teste vrea

- `tari.py` - NU SE MODIFICA

## Pasi pentru incepere proiect

### pentru a face rost de template

```bash
git clone https://github.com/raduionutgavrila/curs_scc_443D_tari.git
git status
git checkout dev-template
git branch dev-nume-prenume
```

### initiere repo local pentru a incarca date in cloud ulterior
```bash
git remote add origin https://github.com/raduionutgavrila/curs_scc_443D_tari.git
```

### pentru a incarca date in cloud
```bash
git add .
git commit -m "<nume branch> - mesaj de commit"
git push
```



## Comenzi GIT

Create a branch: 
```bash
git branch <nume>
```


Rename a branch 
```bash
git branch -m <name>
```

Initiate git in directory: git init

To be able to create a branch you need to:

create a file
Stages the files that will be commited later:
```bash
git add .
```
Commits all the files that are staged
```bash
git commit -m "message"
```
Pull files from github(cloud) to local:
```bash
git pull
```

Push commits to the github repo(cloud) from loca:
```bash
git push -u origin main
```

Connect to online repository
You only need to do this once per project.
```bash
git remote add origin (https://github.com/raduionutgavrila/curs_scc_443D_tari.git)
```


create a branch, while staying on the same branch: 
```bash
git checkout dev
```
create a branch and move to the new one:
```bash
git checkout -b dev
```
Show the current remote origin:
```bash
git remote -v
```

