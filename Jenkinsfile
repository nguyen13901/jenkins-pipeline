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
                sh "docker rm unruffled_herschel -f"
                sh "docker image rm ${DOCKER_IMAGE}:lastest"
                sh "docker build . -t ${DOCKER_IMAGE}:lastest"
            }
        }
        stage("Release") {
            steps {
                sh "docker run -p 8000:8000 ${DOCKER_IMAGE}:lastest"
            }
        }

    //     stage("build") {
    //         agent { node {label ''}}
    //         environment {
    //             DOCKER_TAG="${GIT_BRANCH.tokenize('/').pop()}-${GIT_COMMIT.substring(0,7)}"
    //         }
    //         steps {
    //             sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} . "
    //             sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
    //             sh "docker image ls | grep ${DOCKER_IMAGE}"
    //             withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
    //                 sh 'echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin'
    //                 sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
    //                 sh "docker push ${DOCKER_IMAGE}:latest"
    //             }
    //             //clean to save disk
    //             sh "docker image rm ${DOCKER_IMAGE}:${DOCKER_TAG}"
    //             sh "docker image rm ${DOCKER_IMAGE}:latest"
    //         }
    //     }
    //     stage('deploy server'){
    //         agent { node {label 'dev'}}
    //         environment {
    //             DOCKER_TAG="${GIT_BRANCH.tokenize('/').pop()}-${GIT_COMMIT.substring(0,7)}"
    //         }
    //         steps{
    //             sshagent(credentials:['login_digitalocean']){
    //             sh "ssh  -o StrictHostKeyChecking=no  bangpham@10.104.0.3 sudo docker-compose pull"
    //             sh "ssh  -o StrictHostKeyChecking=no  bangpham@10.104.0.3 sudo docker-compose up -d"
    //             }
    //             echo "success login"
    //         }
    //     }
    // }

    post {
        success {
            echo "SUCCESSFUL"
        }
        failure {
            echo "FAILED"
        }
    }
}
