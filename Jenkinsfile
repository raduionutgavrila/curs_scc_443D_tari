pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Pregatire mediu...'
                sh '''
                    pwd
                    ls -l
                    rm -rf .venv
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                echo 'Verificare cod cu pylint...'
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/tests/*.py
                    pylint --exit-zero tari.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/*.py -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy/containerizare facuta separat cu Dockerfile."
                echo "Build ID: ${BUILD_NUMBER}"
            }
        }
    }
}