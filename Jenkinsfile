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
                    . ./activeaza_venv
                '''
            }
        }
        
        stage('Testare') {
            parallel {
                stage('Pylint - calitate cod') {
                    steps {
                        sh '''
                            . ./activeaza_venv
                            
                            echo "\n\nVerificare app/lib/*.py cu pylint\n"
                            pylint --exit-zero app/lib/*.py

                            echo "\n\nVerificare app/tests/*.py cu pylint"
                            pylint --exit-zero app/tests/*.py

                            echo "\n\nVerificare tari.py cu pylint"
                            pylint --exit-zero tari.py
                        '''
                    }
                }

                stage('Unit Testing cu pytest') {
                    steps {
                        echo 'Unit testing with Pytest...'
                        sh '''
                            . ./activeaza_venv
                            pytest app/tests/*.py -v
                        '''
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker..."
                sh '''
                    docker build -t tari:v${BUILD_NUMBER} .
                    docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
