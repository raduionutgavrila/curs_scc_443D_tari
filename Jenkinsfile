pipeline {
    agent any
    stages {
        stage('Testare Scotia') {
            steps {
                sh 'python3 -m unittest test_tari.py'
            }
        }
    }
}