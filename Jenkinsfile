pipeline {
    agent any
    stages {
        stage('Instalare Dependente') {
            steps {
                sh '''
                chmod +x activeaza_venv activeaza_venv_jenkins || true
                
                bash activeaza_venv
                '''
            }
        }
        stage('Testare') {
            steps {
                sh '''
                . .venv/bin/activate
                
                pytest app/tests
                '''
            }
        }
    }
}