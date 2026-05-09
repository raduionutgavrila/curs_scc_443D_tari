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
                    echo 'Verificare biblioteca Franta...'
                    pylint --exit-zero app/lib/biblioteca_franta.py
                    echo 'Verificare teste Franta...'
                    pylint --exit-zero app/tests/test_lib_franta.py
                '''
            }
        }

        stage('Unit Testing (Pytest)') {
            steps {
                echo 'Executie teste unitare automate...'
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_franta.py -v
                '''
            }
        }

        stage('Docker (Livrare)') {
            steps {
                echo "Numar Build: ${BUILD_NUMBER}"
                echo "Generare imagine si container Docker"
                sh '''
                    docker build -t franta_app:v${BUILD_NUMBER} .
                    docker rm -f tari_container_franta_${BUILD_NUMBER} || true
                    docker create --name tari_container_franta_${BUILD_NUMBER} -p 8020:5011 franta_app:v${BUILD_NUMBER}
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
