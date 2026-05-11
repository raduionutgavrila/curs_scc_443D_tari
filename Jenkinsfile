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
        stage('Deploy') {
            steps {
                sh '''
                sudo docker rm -f container_romania || true
                
                sudo docker build -t imagine_romania .
                
                sudo docker run -d -p 5011:5011 --name container_romania imagine_romania
                '''
            }
        }
    }
}