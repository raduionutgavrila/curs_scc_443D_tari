pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m pip install -r quickrequirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python3 -m pytest app/tests/test_lib_irlanda.py -v'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t proiect-irlanda .'
            }
        }
    }
}
