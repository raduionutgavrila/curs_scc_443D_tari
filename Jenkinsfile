/* Jenkins - Dumitrache Alexandru - Italia */
pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Pregatire mediu de lucru...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv;
                '''
            }
        }

        stage('Verificare calitate cod - pylint') {
            agent any
            steps {
                echo 'Analiza statica a codului cu pylint...'
                sh '''
                    . ./activeaza_venv;
                    echo '\n\nVerificare biblioteca_italia.py cu pylint\n';
                    pylint --exit-zero app/lib/biblioteca_italia.py;

                    echo '\n\nVerificare test_lib_italia.py cu pylint\n';
                    pylint --exit-zero app/tests/test_lib_italia.py;

                    echo '\n\nVerificare tari.py cu pylint\n';
                    pylint --exit-zero tari.py;
                '''
            }
        }

        stage('Teste unitare - pytest') {
            agent any
            steps {
                echo 'Rulare teste unitare pentru Italia...'
                sh '''
                    . ./activeaza_venv;
                    pytest app/tests/test_lib_italia.py -v
                '''
            }
        }
    }
}
