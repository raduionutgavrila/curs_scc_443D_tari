pipeline {
    agent any
    stages {
        stage('Testare Scotia') {
            steps {
                sh 'export PYTHONPATH=$PYTHONPATH:. && python3 app/tests/test_lib_scotia.py'
            }
        }
    }
}