pipeline {
    agent any
    stages{
        stage("Clone source"){
            steps {
                git 'https://github.com/BinhPhanVan/jenkins-pipeline.git'
            }
        }
        stage("Build docker"){
            agent any
            steps {
                withDockerRegistry(credentialsId: 'docker-pipeline', url: 'https://index.docker.io/v1/') {
                    sh 'docker build -t binhphanvan/project-demo:v10 .'
                    sh 'docker push binhphanvan/project-demo:v10'
                }
            }
        }
    } 
}