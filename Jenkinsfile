pipeline {
    agent any
    environment {
        NVD_API_KEY = credentials('NVD-API-KEY')
        // CHROME_DRIVER_PATH = "./chromedriver"
        SONARQUBE_URL = 'http://172.22.0.1:9000'
        SONARQUBE_SCANNER = tool name: 'sonar-scanner'
        SONARQUBE_TOKEN = credentials('SONARQUBE_TOKEN')
    }
    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/Reinakwok/ssd-quiz.git', branch: 'master'
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         script {
        //             dockerImage.inside {
        //                 sh 'pytest --./myapp/junitxml=test-results.xml'
        //             }
        //         }
        //     }
        //     post {
        //         always {
        //             junit 'test-results.xml'
        //         }
        //     }
        // }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQube') {
                        sh '''
                        ${SONARQUBE_SCANNER}/bin/sonar-scanner \
                        -Dsonar.projectKey=SSDPractice \
                        -Dsonar.sources=. \
                        -Dsonar.exclusions=venv/**,dependency-check-report.html,dependency-check-report.xml,pom.xml \
                        -Dsonar.host.url=${SONARQUBE_URL} \
                        -Dsonar.token=${SONARQUBE_TOKEN} \
                        -Dsonar.python.version=3.9
                        '''
                    }
                }
            }
        }

        // stage('OWASP DependencyCheck') {
        //     steps {
        //         dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'owasp'
        //     }
        // }

    }
}
