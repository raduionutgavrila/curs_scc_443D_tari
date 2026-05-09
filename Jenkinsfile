pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                rm -rf .venv
                python3 -m venv .venv
                . .venv/bin/activate
                pip install -r quickrequirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                . .venv/bin/activate
                pytest app/tests/test_lib_spania.py -v
                '''
            }
        }

        stage('Docker build') {
            steps {
                sh 'docker build -t proiect-spania .'
            }
        }
    }
}
