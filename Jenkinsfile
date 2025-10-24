pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "ankushmalgotra/simple-python-app"
        IMAGE_TAG = "v1"
        CONTAINER_NAME = "simple-python-app-container"
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                sh "docker push $IMAGE_NAME:$IMAGE_TAG"
            }
        }

        stage('Run Container Locally') {
            steps {
                // Stop and remove any existing container with same name
                sh "docker stop $CONTAINER_NAME || true"
                sh "docker rm $CONTAINER_NAME || true"

                // Run the container in detached mode
                sh "docker run -d -p 8081:8081 --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG"
            }
        }
    }
}
