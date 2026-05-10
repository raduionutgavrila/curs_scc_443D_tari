/* Jenkins Pipeline testare si deployare aplicatie proiect SCC, Tara: Irlanda */

pipeline {
    agent any

    stages {
        stage('Build and Prep') {
            steps {
                echo "Pregatire mediu: creare .venv si instalare dependinte"
                sh '''
                    chmod +x activeaza_venv_jenkins activeaza_venv ruleaza_aplicatia dockerstart.sh
                    ./activeaza_venv_jenkins
                '''
            }
        }

        stage('Analiza Calitate Cod (Pylint)') {
            steps {
                echo "Analiza statica a codului cu Pylint..."
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/biblioteca_irlanda.py

                    echo "Verificare teste Irlanda..."
                    pylint --exit-zero app/tests/test_lib_irlanda.py
                '''
            }
        }

        stage('Testare Unitare (Pytest)') {
            steps {
                echo "Rulare teste unitare cu Pytest..."
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_irlanda.py -v
                '''
            }
        }

        stage('Lansare Aplicatie in Docker') {
            steps {
                echo "Numar build: ${BUILD_NUMBER}"
                echo "Generare imagine Docker si creare container..."
                sh '''
                    docker build -t irlanda:v${BUILD_NUMBER} .
                    docker create --name tari_container_irlanda_${BUILD_NUMBER} -p 8020:5011 irlanda:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes!'
        }

        failure {
            echo 'Pipeline esuat. Verificati erorile in consola si incercati din nou.'
        }
    }
}
