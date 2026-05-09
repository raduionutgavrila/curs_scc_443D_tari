/* Jenkins*/
pipeline {
    agent any

    stages {
        stage('Build & Prep') {
            steps {
                echo 'Pregatire mediu: Creare .venv si instalare dependinte...'
                sh '''
                    chmod +x activeaza_venv_jenkins activeaza_venv ruleaza_aplicatia dockerstart.sh
                    ./activeaza_venv_jenkins
                '''
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
                    docker create --name tari_container_${BUILD_NUMBER} -p 8020:5011 canada_app:v${BUILD_NUMBER}
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
