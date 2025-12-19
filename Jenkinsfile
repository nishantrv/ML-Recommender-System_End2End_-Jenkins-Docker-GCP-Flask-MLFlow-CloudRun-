pipeline {
  agent any

  environment {
    VENV_DIR    = 'venv'
    GCP_PROJECT = "fluent-protocol-480613-d8"
    GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    REGION      = "us-central1"
    SERVICE     = "ml-project"
    IMAGE       = "gcr.io/fluent-protocol-480613-d8/ml-project:latest"
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

    stage('Setting Up Virtualenv and Installing Dependencies') {
      steps {
        echo 'Setting up virtualenv and installing dependencies...'
        sh '''
          set -eux
          python3 -m venv "${VENV_DIR}"
          . "${VENV_DIR}/bin/activate"
          pip install --upgrade pip
          pip install -e .
        '''
      }
    }

    stage('Build and Push Docker Image (GCR)') {
      steps {
        withCredentials([file(credentialsId: 'gcp-key', variable: 'GCP_KEYFILE')]) {
          echo 'Building and pushing Docker image to GCR...'
          sh '''
            set -eux
            export PATH="$PATH:${GCLOUD_PATH}"

            gcloud auth activate-service-account --key-file="${GCP_KEYFILE}"
            gcloud config set project "${GCP_PROJECT}"

            gcloud auth configure-docker --quiet

            docker build -t "${IMAGE}" .
            docker push "${IMAGE}"
          '''
        }
      }
    }

    stage('Deploy to Cloud Run') {
      steps {
        withCredentials([file(credentialsId: 'gcp-key', variable: 'GCP_KEYFILE')]) {
          echo 'Deploying to Cloud Run...'
          sh '''
            set -eux
            export PATH="$PATH:${GCLOUD_PATH}"

            gcloud auth activate-service-account --key-file="${GCP_KEYFILE}"
            gcloud config set project "${GCP_PROJECT}"

            gcloud run deploy "${SERVICE}" \
              --image="${IMAGE}" \
              --platform=managed \
              --region="${REGION}" \
              --allow-unauthenticated
          '''
        }
      }
    }

  }
}
