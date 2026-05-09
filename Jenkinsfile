/* Jenkins Pipeline testare si deployare aplicatie proiect SCC, Tara: Coreea de Sud */

pipeline {
    agent any

    stages {
        stage('Build and Prep') {
            steps {
                // Checkout cod sursa din repository
                echo "Pregatire mediu: creare .venv si instalare dependinte"
                sh '''
                    chmod +x activeaza_venv_jenkins activeaza_venv ruleaza_aplicatia dockerstart.sh
                    ./activeaza_venv_jenkins
                '''

            }

        }

        stage('Analiza Calitate Cod (Pylint)'){
            steps{
                echo "Analiza statica a codului cu Pylint..."
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app/lib/biblioteca_coreea.py

                    echo "Verificare teste Coreea de Sud..."
                    pylint --exit-zero app/tests/test_lib_coreea.py
                '''

            }

        }
        
        stage('Testare Unitare (Pytest)'){
            steps {
                echo "Rulare teste unitare cu Pytest..."
                sh '''
                    . .venv/bin/activate
                    pytest app/tests/test_lib_coreea.py -v
                '''
            }

        }

        stage('Lansare Aplicatie in Docker') {
            steps {
                echo "Numar build: ${BUILD_NUMBER}"
                echo "Generare imagine Docker si lansare container..."
                sh '''
                    #Construim imaginea folosind Dockerfile-ul creat anterior
                    docker build -t coreea:v${BUILD_NUMBER} .

                    #Cream container 
                    docker create --name tari_container_coreea_${BUILD_NUMBER} -p 8020:5011 coreea:v${BUILD_NUMBER}
                '''

            }
        }


 }

 post {
    success{
        echo 'Pipeline finalizat cu succes! '
        }

    failure{
        echo 'Pipeline esuat. Verificati erorile in consola si incercati din nou.'
    }
 }
}