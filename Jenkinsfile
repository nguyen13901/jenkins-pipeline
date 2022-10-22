pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jenkins-pipeline"
    }
    
    stages{
        stage("Test") {
            steps {
                sh "pip install -r requirements.txt"
                sh "pytest"
            }
        }

        stage("Build") {
            steps {
                script {
                    try {
                        sh "docker rm unruffled_herschel -f"
                        sh "docker image rm ${DOCKER_IMAGE}:lastest"
                    }
                    catch (err) {
                        echo err.getMessage()
                    }
                    sh "docker build . -t ${DOCKER_IMAGE}:lastest"
                }
            }
        }

        stage("Release") {
            steps {
                sh "docker run -p 8000:8000 ${DOCKER_IMAGE}:lastest"
            }
        }
    }

    post {
        success {
            echo "SUCCESSFUL"
        }
        failure {
            echo "FAILED"
        }
    }
}
