pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner-1'
        // Define virtualenv directory
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment and install dependencies
                sh '''
                    /bin/bash -c "python3 -m venv $VENV && source $VENV/bin/activate && pip install -r requirements.txt"
                '''
            }
        }

        stage('Sonar Analysis') {
            steps {
                withSonarQubeEnv('sq1') {
                    // Run SonarQube analysis within the same bash session
                    sh '''
                    /bin/bash -c "source $VENV/bin/activate && sonar-scanner -Dsonar.python.coverage.reportPaths=coverage.xml \
                                  -Dsonar.projectKey=sonar_test \
                                  -Dsonar.host.url=http://192.168.52.92:9000 \
                                  -Dsonar.login=squ_52b64e31e1a72ac2b9fb023ca0b214847d49b7da"
                    '''
                }
            }
        }
    }
    
    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
