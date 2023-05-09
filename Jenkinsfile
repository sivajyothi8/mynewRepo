pipeline {
  agent any
  environment{
    PYTHON_ROOT_DIR='D:/GitHub/DRB-development/venv/Scripts/python.exe'
  }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Checkout') { 
      steps {
checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'jenkin-demo', url: 'https://github.com/sivajyothi8/mynewRepo.git']])
      }
    }
    
    stage('Build'){
      steps {
        // Use a script block to do custom scripting
        script {
            def props = readProperties file: 'extravars.properties' 
            env.Username = props.Username
        }
        echo "The username  is $Username"
    }
      steps{
        git branch: 'main', credentialsId: 'jenkin-demo', url: 'https://github.com/sivajyothi8/mynewRepo.git'
        //bat label:'', script:'C:\\Users\\AIFA USER 29\\AppData\\Local\\Programs\\Python\\Python310\\python.exe main.py'
        bat label:'', script:'`$PYTHON_ROOT_DIR` sample.py'
      }
    }
  }
}
