pipeline {
    agent any

    environment {
        LOG_DIR = '/tmp/advision-logs'
        TIMESTAMP = "${new Date().format('yyyyMMdd-HHmmss')}"
    }

    stages {
        stage('Init') {
            steps {
                sh '''
                if ! command -v python3 > /dev/null; then
                  echo "Python3 is not installed!"
                  exit 1
                fi
                mkdir -p $LOG_DIR
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                python3 -m unittest discover -s tests > $LOG_DIR/test-results-$TIMESTAMP.txt
                '''
            }
        }
        stage('Verify') {
            steps {
                sh '''
                # Example: run flake8 for linting (optional)
                if command -v flake8 > /dev/null; then
                  flake8 . > $LOG_DIR/flake8-$TIMESTAMP.txt || true
                fi
                '''
            }
        }
        stage('Publish') {
            steps {
                archiveArtifacts artifacts: '/tmp/advision-logs/*', fingerprint: true
            }
        }
    }
}