pipeline {
    agent any
    tools {
        jdk 'jdk17'
        maven 'maven3'
    }

    environment {
        SCANNER_HOME=tool 'sonar-scanner-1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        // stage('Build Docker Image') {
        //     steps {
        //         script {
        //             // Define the image name and tag
        //             def appImage = docker.build("flask-app:${env.BUILD_ID}")
        //         }
        //     }
        // }
    
        stage('Test') {
            steps {
                script {
                    echo 'no tests to run'
                }
            }
        }
        // stage('Push Image') {
        //     steps {
        //         script {
        //             echo 'Pushing to registry ...'
        //             // docker.withRegistry('https://registry.hub.docker.com', 'docker-credentials-id') {
        //             //     appImage.push("${env.BUILD_ID}")
        //             //     appImage.push("latest")
        //             // }
        //         }
        //     }
        // }
        stage('Sonar Analysis') {
            steps {
                withSonarQubeEnv('sonar-server-1') {
                sh "mvn clean verify"
                sh ''' mvn sonar:sonar -Dsonar-url=http://192.168.52.92:9000/ \
                -Dsonar.login=squ_52b64e31e1a72ac2b9fb023ca0b214847d49b7da -Dsonar.projectName=sonar_test \
                -Dsonar.Java.binaries=. -Dsonar.projectKey=sonar_test '''
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
