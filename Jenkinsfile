pipeline {
    agent any

    stages {
        stage('Pregatire proiect') {
            steps {
                echo 'Pregatire proiect SCC - Elvetia - Tecsan Calin'
                sh '''
                    pwd
                    ls -l
                    . ./activeaza_venv_jenkins
                    python --version
                    pip --version
                '''
            }
        }

        stage('Pylint - verificare cod') {
            steps {
                echo 'Verificare calitate cod pentru fisierele proiectului Elvetia'
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=$WORKSPACE

                    echo "\\nVerificare biblioteca_elvetia.py"
                    pylint --exit-zero app/lib/biblioteca_elvetia.py

                    echo "\\nVerificare biblioteca_tari.py"
                    pylint --exit-zero app/lib/biblioteca_tari.py

                    echo "\\nVerificare test_lib_elvetia.py"
                    pylint --exit-zero app/tests/test_lib_elvetia.py

                    echo "\\nVerificare tari.py"
                    pylint --exit-zero tari.py
                '''
            }
        }

        stage('Unit Testing cu Pytest') {
            steps {
                echo 'Rulare teste unitare pentru Elvetia'
                sh '''
                    . .venv/bin/activate
                    export PYTHONPATH=$WORKSPACE

                    pytest app/tests/test_lib_elvetia.py -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo "Creare imagine Docker pentru build ${BUILD_NUMBER}"
                sh '''
                    docker build -t tari-elvetia-tecsan-calin:v${BUILD_NUMBER} .
                    docker images | grep tari-elvetia-tecsan-calin
                '''
            }
        }

        stage('Docker Run') {
            steps {
                echo "Pornire container Docker pentru build ${BUILD_NUMBER}"
                sh '''
                    docker rm -f tari-elvetia-tecsan-calin || true
                    docker run -d --name tari-elvetia-tecsan-calin -p 8020:5011 tari-elvetia-tecsan-calin:v${BUILD_NUMBER}
                    docker ps | grep tari-elvetia-tecsan-calin
                '''
            }
        }
    }
}
