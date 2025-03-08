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
        success {
            echo 'Pipeline executado com sucesso! Contêiner está em execução.'
        }
        failure {
            echo 'Pipeline falhou! Parando e removendo contêiner.'
            sh 'docker-compose down'
        }
    }

}
