pipeline {
    agent any
    stages {
        stage('Testare Scotia') {
            steps {
                sh 'export PYTHONPATH=$PYTHONPATH:. && python3 -m unittest test_tari.py'
            }
        }
    }
}