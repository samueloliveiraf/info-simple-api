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

        stage('Build Docker Image') {
            steps {
                script {
                    // Construir a imagem Docker
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Rodar os testes (ajuste se necessário para o framework de testes)
                    sh 'pytest'  // Se você não tiver pytest, substitua por outros testes
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // Rodar o Docker Compose para rodar a aplicação
                    sh 'docker-compose -f docker-compose.yml up -d --build'
                }
            }
        }
    }

    post {
        always {
            // Limpar a imagem Docker após o pipeline (opcional)
            sh 'docker rmi $DOCKER_IMAGE:$DOCKER_TAG'
        }

        success {
            echo 'Pipeline executado com sucesso!'
        }

        failure {
            echo 'Pipeline falhou!'
        }
    }
}
