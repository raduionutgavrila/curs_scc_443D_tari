/*Jenkins*/
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . .venv/bin/activate
                    echo "Verificare app/lib/*.py cu pylint"
                    pylint --exit-zero app/lib/*.py
                    echo "Verificare app/tests/*.py cu pylint"
                    pylint --exit-zero app/tests/*.py
                    echo "Verificare tari.py cu pylint"
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
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker rm -f tari${BUILD_NUMBER} 2>/dev/null || true
                    docker build -t tari:v${BUILD_NUMBER} .
                    docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
