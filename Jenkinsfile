<<<<<<< HEAD
<<<<<<< HEAD
/*Jenkins*/
=======
/* Jenkins Pipeline testare si deployare aplicatie proiect SCC, Tara: Irlanda */

>>>>>>> origin/main_pirjol_mara
=======
>>>>>>> origin/main_tecsan_calin
pipeline {
    agent any

    stages {
<<<<<<< HEAD
<<<<<<< HEAD
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv;
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
                '''
            }
        }

<<<<<<< HEAD
<<<<<<< HEAD
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
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
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
                '''
            }
        }

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
                '''
            }
        }

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
                '''
            }
        }
    }
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
