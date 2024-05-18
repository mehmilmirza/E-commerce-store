pipeline {
    agent {
        docker {
            image 'node:14'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        DB_URL = 'mongodb+srv://mehmilmirz:r1ysqPaa2GzYyG6m@devopscluster.qumtt9x.mongodb.net/eStore'
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/mehmilmirza/E-commerce-store.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Run tests') {
            steps {
                sh 'npm test'
            }
        }
        stage('Build') {
            steps {
                sh 'npm run build'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def appName = 'e-commerce-store'
                    def appVersion = 'latest'
                    sh "docker build -t ${appName}:${appVersion} ."
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
