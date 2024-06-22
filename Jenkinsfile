pipeline {
    agent any

    environment {
        some_key = credentials('something')
    }

    stages {
        stage('Run Athena Query') {
            steps {
                script {
                    bat '''
                    set some_key=%some_key%
                    python env_check.py
                    '''
                }
            }
        }
    }
}
