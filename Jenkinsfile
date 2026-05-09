<<<<<<< HEAD
/* Jenkins Pipeline testare si deployare aplicatie proiect SCC, Tara: Coreea de Sud */

=======
/* Jenkins*/
>>>>>>> origin/dev_roseanu_vlad
pipeline {
    agent any

    stages {
<<<<<<< HEAD
        stage('Build and Prep') {
            steps {
                // Checkout cod sursa din repository
                echo "Pregatire mediu: creare .venv si instalare dependinte"
=======
        stage('Build & Prep') {
            steps {
                echo 'Pregatire mediu: Creare .venv si instalare dependinte...'
>>>>>>> origin/dev_roseanu_vlad
                sh '''
                    chmod +x activeaza_venv_jenkins activeaza_venv ruleaza_aplicatia dockerstart.sh
                    ./activeaza_venv_jenkins
                '''
<<<<<<< HEAD

            }

        }

        stage('Analiza Calitate Cod (Pylint)'){
            steps{
                echo "Analiza statica a codului cu Pylint..."
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/biblioteca_coreea.py

                    echo "Verificare teste Coreea de Sud..."
                    pylint --exit-zero app/tests/test_lib_coreea.py
                '''

            }

        }
        
        stage('Testare Unitare (Pytest)'){
            steps {
                echo "Rulare teste unitare cu Pytest..."
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_coreea.py -v
                '''
            }

        }

        stage('Lansare Aplicatie in Docker') {
            steps {
                echo "Numar build: ${BUILD_NUMBER}"
                echo "Generare imagine Docker si lansare container..."
                sh '''
                    #Construim imaginea folosind Dockerfile-ul creat anterior
                    docker build -t coreea:v${BUILD_NUMBER} .

                    #Cream container 
                    docker create --name tari_container_coreea_${BUILD_NUMBER} -p 8020:5011 coreea:v${BUILD_NUMBER}
                '''

            }
        }


 }

 post {
    success{
        echo 'Pipeline finalizat cu succes! '
        }

    failure{
        echo 'Pipeline esuat. Verificati erorile in consola si incercati din nou.'
    }
 }
}
=======
            }
        }

        stage('Calitate Cod (Pylint)') {
            steps {
                echo 'Analiza statica a codului...'
                sh '''
                    . .venv/bin/activate
                    echo 'Verificare biblioteca Canada...'
                    pylint --exit-zero app/lib/biblioteca_canada.py
                    echo 'Verificare teste Canada...'
                    pylint --exit-zero app/tests/test_lib_canada.py
                '''
            }
        }

        stage('Unit Testing (Pytest)') {
            steps {
                echo 'Executie teste unitare automate...'
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_canada.py -v
                '''
            }
        }

        stage('Docker (Livrare)') {
            steps {
                echo "Numar Build: ${BUILD_NUMBER}"
                echo "Generare imagine si container Docker"
                sh '''
                    docker build -t canada_app:v${BUILD_NUMBER} .
                    docker rm -f tari_container_${BUILD_NUMBER} || true
                    docker create --name tari_container_${BUILD_NUMBER} -p 5011:5011 canada_app:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes (PASS)! '
        }
        failure {
            echo 'Eroare in pipeline. Verifica log-urile de consola.'
        }
    }
}
>>>>>>> origin/dev_roseanu_vlad
