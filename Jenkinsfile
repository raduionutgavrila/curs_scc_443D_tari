<<<<<<< HEAD
<<<<<<< HEAD

/*Jenkins*/

=======
/* Jenkins Pipeline Declarativ - Grupa 443D - Subiect: Statele Unite */
>>>>>>> origin/main_esterabadeyan_hadi
=======
/Jenkins/
>>>>>>> origin/main_zidu_cristian
pipeline {
    agent any

    stages {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main_zidu_cristian
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
                    . ./activeaza_venv_jenkins
>>>>>>> origin/main_zidu_cristian
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
        stage('Build & Prep') {
            steps {
                echo 'Pregatire mediu: Creare .venv si instalare dependinte...'
                sh '''
                    chmod +x activeaza_venv_jenkins activeaza_venv ruleaza_aplicatia dockerstart.sh
                    ./activeaza_venv_jenkins
>>>>>>> origin/main_esterabadeyan_hadi
=======
>>>>>>> origin/main_zidu_cristian
                '''
            }
        }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main_zidu_cristian
        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv;
<<<<<<< HEAD
                    pytest app/tests/*.py -v
=======
                    pytest app/tests/test_lib_estonia.py -v
>>>>>>> origin/main_zidu_cristian

                    
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
<<<<<<< HEAD
=======
        stage('Teste unitare - pytest') {
            agent any
            steps {
                echo 'Rulare teste unitare pentru Italia...'
                sh '''
                    . .venv/bin/activate;
                    pytest app/tests/test_lib_italia.py -v
>>>>>>> origin/main_dumitrache_alexandru
=======
        stage('Calitate Cod (Pylint)') {
            steps {
                echo 'Analiza statica a codului...'
                sh '''
                    . .venv/bin/activate
                    echo 'Verificare biblioteca Statele Unite...'
                    pylint --exit-zero app/lib/biblioteca_statele_unite.py
                    
                    echo 'Verificare teste Statele Unite...'
                    pylint --exit-zero app/tests/test_lib_statele_unite.py
                '''
            }
        }

        stage('Unit Testing (Pytest)') {
            steps {
                echo 'Executie teste unitare automate...'
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_statele_unite.py -v
                '''
            }
        }

        stage('Docker (Livrare)') {
            steps {
                echo "Numar Build: ${BUILD_NUMBER}"
                echo "Generare imagine si container Docker"
                sh '''
                    # Construim imaginea folosind Dockerfile-ul creat anterior
                    docker build -t sua_app:v${BUILD_NUMBER} .
                    
                    # Optional: Curatam containerele vechi cu acelasi nume pentru a evita erorile
                    docker rm -f tari_container_${BUILD_NUMBER} || true
                    
                    # Cream containerul
                    docker create --name tari_container_${BUILD_NUMBER} -p 8020:5011 sua_app:v${BUILD_NUMBER}
>>>>>>> origin/main_esterabadeyan_hadi
=======
>>>>>>> origin/main_zidu_cristian
                '''
            }
        }
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
}
=======
}
>>>>>>> origin/main_dumitrache_alexandru
=======

    post {
        success {
            echo 'Pipeline finalizat cu succes (PASS)! '
        }
        failure {
            echo 'Eroare in pipeline. Verifica log-urile de consola.'
        }
    }
}
>>>>>>> origin/main_esterabadeyan_hadi
=======
}
>>>>>>> origin/main_zidu_cristian
