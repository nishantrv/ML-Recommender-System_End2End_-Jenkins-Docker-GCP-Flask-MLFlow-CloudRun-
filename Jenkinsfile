pipeline {
  agent any

  environment {
    VENV_DIR    = 'venv'
    GCP_PROJECT = "fluent-protocol-480613-d8"
    GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
  }

  stages {

    stage('Cloning Github Repo to Jenkins') {
      steps {
        echo 'Cloning Github from Jenkins.......'
        checkout scmGit(
          branches: [[name: '*/main']],
          extensions: [],
          userRemoteConfigs: [[
            credentialsId: 'github-token',
            url: 'https://github.com/nishantrv/ML-Recommender-System_End2End_-Jenkins-Docker-GCP-Flask-MLFlow-CloudRun-.git'
          ]]
        )
      }
    }

    stage('Setting Up our virtual environment and Installing Dependencies') {
      steps {
        echo 'Setting Up our virtual environment and Installing Dependencies.......'
        sh '''
          set -eux
          python3 -m venv "${VENV_DIR}"
          . "${VENV_DIR}/bin/activate"
          pip install --upgrade pip
          pip install -e .
        '''
      }
    }

    stage('Building and Pushing Docker Image to GCR') {
      steps {
        withCredentials([file(credentialsId: 'gcp-key', variable: 'GCP_KEYFILE')]) {
          echo 'Building and Pushing Docker Image to GCR'
          sh '''
            set -eux
            export PATH="$PATH:${GCLOUD_PATH}"

            gcloud auth activate-service-account --key-file="${GCP_KEYFILE}"
            gcloud config set project "${GCP_PROJECT}"

            gcloud auth configure-docker --quiet

            docker build -t "gcr.io/${GCP_PROJECT}/ml-project:latest" .
            docker push "gcr.io/${GCP_PROJECT}/ml-project:latest"
          '''
        }
      }
    }

  }
}
