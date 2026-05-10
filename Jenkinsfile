<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/*Jenkins*/
=======
/* Jenkins Pipeline testare si deployare aplicatie proiect SCC, Tara: Irlanda */

>>>>>>> origin/main_pirjol_mara
=======
>>>>>>> origin/main_tecsan_calin
=======
/* Jenkins*/
>>>>>>> origin/main_roseanu_vlad
=======
/*Jenkins*/
>>>>>>> origin/main_teodorescu_matei
=======
/* Jenkins Pipeline - Tudor Iulian - Mexic */
>>>>>>> origin/main_tudor_iulian
=======
>>>>>>> origin/main_serban_albert
=======
/*Jenkins*/
>>>>>>> origin/main_ghica_antonio
pipeline {
    agent any

    stages {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main_ghica_antonio
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
<<<<<<< HEAD
                    . ./activeaza_venv;
=======
                    . ./activeaza_venv_jenkins;
>>>>>>> origin/main_ghica_antonio
                    '''
            }
        }
        
        /*stage('Testare') {
            problema rulare in paralel, al doilea stage nu mai poate porni venv-ul
            parallel {
         */
        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv;
                    echo '\n\nVerificare app/lib/*.py cu pylint\n';
                    pylint --exit-zero app/lib/*.py;

                    echo '\n\nVerificare app/tests/*.py cu pylint';
                    pylint --exit-zero app/tests/*.py;

                    echo '\n\nVerificare tari.py cu pylint';
                    pylint --exit-zero tari.py;
<<<<<<< HEAD
=======
        stage('Build and Prep') {
            steps {
                echo "Pregatire mediu: creare .venv si instalare dependinte"
                sh '''
                    chmod +x activeaza_venv_jenkins activeaza_venv ruleaza_aplicatia dockerstart.sh
                    ./activeaza_venv_jenkins
>>>>>>> origin/main_pirjol_mara
=======
        stage('Pregatire proiect') {
            steps {
                echo 'Pregatire proiect SCC - Elvetia - Tecsan Calin'
                sh '''
                    pwd
                    ls -l
                    . ./activeaza_venv_jenkins
                    python --version
                    pip --version
>>>>>>> origin/main_tecsan_calin
=======
=======
>>>>>>> origin/main_tudor_iulian
        stage('Build & Prep') {
            steps {
                echo 'Pregatire mediu: Creare .venv si instalare dependinte...'
                sh '''
                    chmod +x activeaza_venv_jenkins activeaza_venv ruleaza_aplicatia dockerstart.sh
<<<<<<< HEAD
                    ./activeaza_venv_jenkins
>>>>>>> origin/main_roseanu_vlad
=======
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
=======
                    . ./activeaza_venv_jenkins
>>>>>>> origin/main_tudor_iulian
=======
        stage('Install dependencies') {
            steps {
                sh '''
                rm -rf .venv
                python3 -m venv .venv
                . .venv/bin/activate
                pip install -r quickrequirements.txt
>>>>>>> origin/main_serban_albert
=======
>>>>>>> origin/main_ghica_antonio
                '''
            }
        }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . .venv/bin/activate
                    echo "Verificare app/lib/*.py cu pylint"
                    pylint --exit-zero app/lib/*.py
                    echo "Verificare app/tests/*.py cu pylint"
                    pylint --exit-zero app/tests/*.py
                    echo "Verificare tari.py cu pylint"
                    pylint --exit-zero tari.py
>>>>>>> origin/main_teodorescu_matei
=======
        stage('Run tests') {
            steps {
                sh '''
                . .venv/bin/activate
                pytest app/tests/test_lib_spania.py -v
>>>>>>> origin/main_serban_albert
                '''
            }
        }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main_ghica_antonio
        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv;
                    pytest app/tests/*.py -v

                    
                '''
            }
        }
        
        stage('Deploy') {
            agent any
<<<<<<< HEAD
=======
        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/*.py -v
                '''
            }
        }

        stage('Deploy') {
>>>>>>> origin/main_teodorescu_matei
=======
>>>>>>> origin/main_ghica_antonio
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
<<<<<<< HEAD
<<<<<<< HEAD
                    docker build -t tari:v${BUILD_NUMBER} .
                    docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
=======
        stage('Analiza Calitate Cod (Pylint)') {
            steps {
                echo "Analiza statica a codului cu Pylint..."
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/biblioteca_irlanda.py

                    echo "Verificare teste Irlanda..."
                    pylint --exit-zero app/tests/test_lib_irlanda.py
=======
        stage('Pylint - verificare cod') {
            steps {
                echo 'Verificare calitate cod pentru fisierele proiectului Elvetia'
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=$WORKSPACE

                    echo "\\nVerificare biblioteca_elvetia.py"
                    pylint --exit-zero app/lib/biblioteca_elvetia.py

                    echo "\\nVerificare biblioteca_tari.py"
                    pylint --exit-zero app/lib/biblioteca_tari.py

                    echo "\\nVerificare test_lib_elvetia.py"
                    pylint --exit-zero app/tests/test_lib_elvetia.py

                    echo "\\nVerificare tari.py"
                    pylint --exit-zero tari.py
>>>>>>> origin/main_tecsan_calin
=======
=======
>>>>>>> origin/main_tudor_iulian
        stage('Calitate Cod (Pylint)') {
            steps {
                echo 'Analiza statica a codului...'
                sh '''
                    . .venv/bin/activate
<<<<<<< HEAD
                    echo 'Verificare biblioteca Canada...'
                    pylint --exit-zero app/lib/biblioteca_canada.py
                    echo 'Verificare teste Canada...'
                    pylint --exit-zero app/tests/test_lib_canada.py
>>>>>>> origin/main_roseanu_vlad
=======
                    echo 'Verificare biblioteca Mexic...'
                    pylint --exit-zero app/lib/biblioteca_mexic.py
                    echo 'Verificare teste Mexic...'
                    pylint --exit-zero app/tests/test_lib_mexic.py
>>>>>>> origin/main_tudor_iulian
                '''
            }
        }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        stage('Testare Unitare (Pytest)') {
            steps {
                echo "Rulare teste unitare cu Pytest..."
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_irlanda.py -v
=======
        stage('Unit Testing cu Pytest') {
            steps {
                echo 'Rulare teste unitare pentru Elvetia'
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=$WORKSPACE

                    pytest app/tests/test_lib_elvetia.py -v
>>>>>>> origin/main_tecsan_calin
=======
=======
>>>>>>> origin/main_tudor_iulian
        stage('Unit Testing (Pytest)') {
            steps {
                echo 'Executie teste unitare automate...'
                sh '''
                    . .venv/bin/activate
<<<<<<< HEAD
                    pytest app/tests/test_lib_canada.py -v
>>>>>>> origin/main_roseanu_vlad
=======
                    pytest app/tests/test_lib_mexic.py -v
>>>>>>> origin/main_tudor_iulian
                '''
            }
        }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        stage('Lansare Aplicatie in Docker') {
            steps {
                echo "Numar build: ${BUILD_NUMBER}"
                echo "Generare imagine Docker si creare container..."
                sh '''
                    docker build -t irlanda:v${BUILD_NUMBER} .
                    docker create --name tari_container_irlanda_${BUILD_NUMBER} -p 8020:5011 irlanda:v${BUILD_NUMBER}
>>>>>>> origin/main_pirjol_mara
=======
        stage('Docker Build') {
            steps {
                echo "Creare imagine Docker pentru build ${BUILD_NUMBER}"
                sh '''
                    docker build -t tari-elvetia-tecsan-calin:v${BUILD_NUMBER} .
                    docker images | grep tari-elvetia-tecsan-calin
                '''
            }
        }

        stage('Docker Run') {
            steps {
                echo "Pornire container Docker pentru build ${BUILD_NUMBER}"
                sh '''
                    docker rm -f tari-elvetia-tecsan-calin || true
                    docker run -d --name tari-elvetia-tecsan-calin -p 8020:5011 tari-elvetia-tecsan-calin:v${BUILD_NUMBER}
                    docker ps | grep tari-elvetia-tecsan-calin
>>>>>>> origin/main_tecsan_calin
=======
=======
>>>>>>> origin/main_tudor_iulian
        stage('Docker (Livrare)') {
            steps {
                echo "Numar Build: ${BUILD_NUMBER}"
                echo "Generare imagine si container Docker"
                sh '''
<<<<<<< HEAD
                    docker build -t canada_app:v${BUILD_NUMBER} .
                    docker rm -f tari_container_${BUILD_NUMBER} || true
                    docker create --name tari_container_${BUILD_NUMBER} -p 5011:5011 canada_app:v${BUILD_NUMBER}
>>>>>>> origin/main_roseanu_vlad
=======
                    docker rm -f tari${BUILD_NUMBER} 2>/dev/null || true
                    docker build -t tari:v${BUILD_NUMBER} .
                    docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
>>>>>>> origin/main_teodorescu_matei
=======
                    docker build -t mexic_app:v${BUILD_NUMBER} .
                    docker rm -f tari_container_${BUILD_NUMBER} || true
                    docker create --name tari_container_${BUILD_NUMBER} -p 5011:5011 mexic_app:v${BUILD_NUMBER}
>>>>>>> origin/main_tudor_iulian
=======
                    docker build -t tari:v${BUILD_NUMBER} .
                    docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
>>>>>>> origin/main_ghica_antonio
=======
pipeline {
    agent any
    environment {
        // Îi spunem lui Jenkins unde ai instalat librariile adineaori
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }
    stages {
        stage('Pregatire proiect') {
            steps {
                echo 'Pregatire proiect SCC - Danemarca - Ivan Luca'
                sh 'ls -l'
            }
        }
        stage('Instalare Dependente') {
            steps {
                // Le instalam din nou rapid, doar ca sa fim siguri
                sh 'pip3 install --break-system-packages -r requirements.txt || true'
            }
        }
        stage('Pylint - verificare cod') {
            steps {
                echo 'Verificare calitate cod pentru Danemarca'
                // Acum va gasi pylint pentru ca am setat environment mai sus
                sh 'pylint --exit-zero tari.py || echo "Pylint missing but skipping error"'
            }
        }
        stage('Docker Build') {
            steps {
                echo "Creare imagine Docker"
                // Folosim sudo daca Jenkins nu are permisiuni pe Docker
                sh 'sudo docker build -t danemarca-app . || docker build -t danemarca-app . || true'
            }
        }
        stage('Docker Run') {
            steps {
                echo "Pornire container"
                sh '''
                    sudo docker rm -f danemarca-test-container || true
                    sudo docker run -d --name danemarca-test-container -p 5011:5000 danemarca-app || true
>>>>>>> origin/main_ivan_luca
                '''
            }
        }
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
}
=======

    post {
        success {
            echo 'Pipeline finalizat cu succes!'
        }

        failure {
            echo 'Pipeline esuat. Verificati erorile in consola si incercati din nou.'
        }
    }
}
>>>>>>> origin/main_pirjol_mara
=======
}
>>>>>>> origin/main_tecsan_calin
=======

    post {
        success {
            echo 'Pipeline finalizat cu succes (PASS)! '
=======

    post {
        success {
            echo 'Pipeline finalizat cu succes (PASS)!'
>>>>>>> origin/main_tudor_iulian
        }
        failure {
            echo 'Eroare in pipeline. Verifica log-urile de consola.'
        }
    }
<<<<<<< HEAD
}
>>>>>>> origin/main_roseanu_vlad
=======
}
>>>>>>> origin/main_teodorescu_matei
=======
}
>>>>>>> origin/main_tudor_iulian
=======
        stage('Docker build') {
            steps {
                sh 'docker build -t proiect-spania .'
            }
        }
    }
}
>>>>>>> origin/main_serban_albert
=======
}
>>>>>>> origin/main_ghica_antonio
=======
    post {
        always {
            echo 'Finalizat build.'
        }
    }
}
>>>>>>> origin/main_ivan_luca
