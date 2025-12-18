pipeline{
    agent any
    
    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "fluent-protocol-480613-d8"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Cloning Github Repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github from Jenkins.......'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/nishantrv/ML-Recommender-System_End2End_-Jenkins-Docker-GCP-Flask-MLFlow-CloudRun-.git']])           
                }
            }
        }
    stage('Setting Up our virtual environment and Installing Dependencies'){
            steps{
                script{
                    echo 'Setting Up our virtual environment and Installing Dependencies.......'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
    stage('Building and Pushing Docker Image to GCR'){
            steps{
                script{
                    withCredentials([file(credentialsId: 'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                        script{
                            echo 'Building and Pushing Docker Image to GCR'
                            sh '''
                            export PATH=$PATH:${GCLOUD_PATH}

                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                            gcloud config set project ${GCP_PROJECT}

                            gcloud auth configure-docker --quiet

                            docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                            docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                            '''
                        }
                    }
                }
            }
        }
    }
}

