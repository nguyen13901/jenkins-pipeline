pipeline {
    agent any
    stages{
        stage("Clone source"){
            steps {
                git 'https://github.com/BinhPhanVan/jenkins-pipeline.git'
            }
        }
        stage("Build docker"){
            steps {
                sh 'docker build -t project-demo .'
                sh 'docker run -dp 7009:8000 project-demo'
            }
        }
    }
}