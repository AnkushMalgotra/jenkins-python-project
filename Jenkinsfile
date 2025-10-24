pipeline {
    agent any

    environment {
        IMAGE = "ankushmalgotra/simple-python-app"
        TAG = "v${env.BUILD_NUMBER}"
    }

    stages {
        stage('Ankush Malgotra - Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE}:${TAG} .'
            }
        }

        stage('Ankush Malgotra - Login to Dockerhub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Ankush Malgotra - Push image to Dockerhub') {
            steps {
                sh 'docker push ${IMAGE}:${TAG}'
            }
        }
    }
}
