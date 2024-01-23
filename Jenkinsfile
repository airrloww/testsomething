pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Define the image name and tag
                    def appImage = docker.build("flask-app:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests here
                    echo 'no tests to run'
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    echo 'Pushing to registry ...'
                    // docker.withRegistry('https://registry.hub.docker.com', 'docker-credentials-id') {
                    //     appImage.push("${env.BUILD_ID}")
                    //     appImage.push("latest")
                    // }
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
