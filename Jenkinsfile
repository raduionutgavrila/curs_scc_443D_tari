pipeline {
    agent any
    stages {
        stage('Instalare Dependente') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Testare') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}