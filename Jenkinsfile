pipeline {
    agent any
    stages {
        stage('Instalare Dependente') {
            steps {
                sh '''
                chmod +x activeaza_venv.sh activeaza_venv_jenkins || true
                
                bash activeaza_venv.sh
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