/* Jenkins Pipeline testare si deployare aplicatie proiect SCC, Tara: Finlanda */

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
                    pylint --exit-zero app/lib/biblioteca_finlanda.py

                    echo "Verificare teste Finlanda..."
                    pylint --exit-zero app/tests/test_lib_finlanda.py
                '''
            }
        }

        stage('Testare Unitare (Pytest)') {
            steps {
                echo "Rulare teste unitare cu Pytest..."
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_finlanda.py -v
                '''
            }
        }

        stage('Lansare Aplicatie in Docker') {
            steps {
                echo "Numar build: ${BUILD_NUMBER}"
                echo "Generare imagine Docker si lansare container..."
                sh '''
                    docker build -t finlanda:v${BUILD_NUMBER} .

                    docker create --name tari_container_finlanda_${BUILD_NUMBER} -p 8020:5011 finlanda:v${BUILD_NUMBER}
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
