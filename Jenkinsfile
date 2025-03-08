pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'fastapi-infosimpleapi'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build and Deploy with Docker Compose') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml build'
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'

            sh 'docker rmi api-info-simple-fastapi:latest'
        }

        success {
            echo 'Pipeline executado com sucesso!'
        }

        failure {
            echo 'Pipeline falhou!'
        }
    }
}
