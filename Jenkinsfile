/* Jenkins */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    python3 --version
                    rm -rf .venv
                    python3 -m venv .venv
                    . .venv/bin/activate && pip install --upgrade pip
                    . .venv/bin/activate && pip install -r quickrequirements.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                echo 'Verificare calitate cod cu pylint...'
                sh '''
                    . .venv/bin/activate && echo "\\n\\nVerificare app/lib/*.py cu pylint\\n"
                    . .venv/bin/activate && pylint --exit-zero app/lib/*.py

                    . .venv/bin/activate && echo "\\n\\nVerificare app/tests/*.py cu pylint\\n"
                    . .venv/bin/activate && pylint --exit-zero app/tests/*.py

                    . .venv/bin/activate && echo "\\n\\nVerificare tari.py cu pylint\\n"
                    . .venv/bin/activate && pylint --exit-zero tari.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . .venv/bin/activate && pytest app/tests/*.py -v
                '''
            }
        }

        /* Jenkins */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    python3 --version
                    rm -rf .venv
                    python3 -m venv .venv
                    . .venv/bin/activate && pip install --upgrade pip
                    . .venv/bin/activate && pip install -r quickrequirements.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                echo 'Verificare calitate cod cu pylint...'
                sh '''
                    . .venv/bin/activate && echo "\\n\\nVerificare app/lib/*.py cu pylint\\n"
                    . .venv/bin/activate && pylint --exit-zero app/lib/*.py

                    . .venv/bin/activate && echo "\\n\\nVerificare app/tests/*.py cu pylint\\n"
                    . .venv/bin/activate && pylint --exit-zero app/tests/*.py

                    . .venv/bin/activate && echo "\\n\\nVerificare tari.py cu pylint\\n"
                    . .venv/bin/activate && pylint --exit-zero tari.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . .venv/bin/activate && pytest app/tests/*.py -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Deploy/containerizare verificata separat prin Dockerfile."
                echo "Imaginea Docker a fost construita manual cu: sudo docker build -t proiect-scc-japonia ."
                echo "Containerul a fost rulat manual cu: sudo docker run --rm -p 5011:5011 proiect-scc-japonia"
            }
        }
    }
}