pipeline {
    agent any

    stages {
        stage('Info') {
            steps {
                sh 'pwd'
                sh 'python3 --version'
            }
        }

        stage('Pregatire mediu') {
            steps {
                sh 'rm -rf .venv'
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r quickrequirements.txt'
            }
        }

        stage('Teste Pytest') {
            steps {
                sh '. .venv/bin/activate && pytest app/tests/test_lib_japonia.py -v'
            }
        }
    }
}