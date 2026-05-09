pipeline {
    agent any
    stages {
        stage('Instalare Dependente') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
            }
        }
        stage('Rulare Teste') {
            steps {
                sh 'python3 -m pytest app/tests/'
            }
        }
    }
}
