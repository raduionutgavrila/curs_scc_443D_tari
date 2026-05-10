<<<<<<< HEAD

/*Jenkins*/

=======
/* Jenkins */
>>>>>>> origin/main_ciobanu_andrei
pipeline {
    agent any

    stages {
        stage('Build') {
<<<<<<< HEAD
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv;
                    '''
            }
        }
        
        /*stage('Testare') {
            problema rulare in paralel, al doilea stage nu mai poate porni venv-ul
            parallel {
         */
        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv;
                    echo '\n\nVerificare app/lib/*.py cu pylint\n';
                    pylint --exit-zero app/lib/*.py;

                    echo '\n\nVerificare app/tests/*.py cu pylint';
                    pylint --exit-zero app/tests/*.py;

                    echo '\n\nVerificare tari.py cu pylint';
                    pylint --exit-zero tari.py;
=======
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
>>>>>>> origin/main_ciobanu_andrei
                '''
            }
        }

        stage('Unit Testing cu pytest') {
<<<<<<< HEAD
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . ./activeaza_venv;
                    pytest app/tests/*.py -v

                    
                '''
            }
        }
        
=======
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . .venv/bin/activate && pytest app/tests/*.py -v
                '''
            }
        }

>>>>>>> origin/main_ciobanu_andrei
        stage('Deploy') {
            agent any
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t tari:v${BUILD_NUMBER} .
                    docker create --name tari${BUILD_NUMBER} -p 8020:5011 tari:v${BUILD_NUMBER}
                '''
            }
        }
<<<<<<< HEAD
    }
=======
}
>>>>>>> origin/main_ciobanu_andrei
}