pipeline {
    agent any

    stages {
        stage('Pregatire proiect') {
            steps {
                echo 'Pregatire proiect SCC - Danemarca - Ivan Luca'
                sh '''
                    pwd
                    ls -l
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Instalare Dependente') {
            steps {
                echo 'Instalare librarii necesare'
                // Folosim --break-system-packages pentru a trece de protectia Python 3.12
                sh 'pip3 install --break-system-packages -r requirements.txt || true'
            }
        }

        stage('Pylint - verificare cod') {
            steps {
                echo 'Verificare calitate cod pentru Danemarca'
                sh '''
                    export PYTHONPATH=$WORKSPACE
                    pylint --exit-zero tari.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo "Creare imagine Docker pentru Danemarca"
                // Folosim numele imaginii tale din README
                sh 'docker build -t danemarca-app .'
            }
        }

        stage('Docker Run') {
            steps {
                echo "Pornire container de test"
                sh '''
                    docker rm -f danemarca-test-container || true
                    docker run -d --name danemarca-test-container -p 5011:5000 danemarca-app
                    docker ps | grep danemarca-test-container
                '''
            }
        }
    }

    post {
        success {
            echo 'Build-ul a fost finalizat cu succes!'
        }
        failure {
            echo 'Build-ul a esuat. Verifica log-urile de mai sus.'
        }
    }
}
