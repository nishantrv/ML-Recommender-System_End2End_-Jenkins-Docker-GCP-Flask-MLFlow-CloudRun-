pipeline{
    agent any

    stages{
        stage('Cloning Github Repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github from Jenkins.......'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/nishantrv/ML-Recommender-System_End2End_-Jenkins-Docker-GCP-Flask-MLFlow-CloudRun-.git']])           
                }
            }
        }
    }
}

