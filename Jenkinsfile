node('slave1'){
  def svcName = 'products'
  def nsName = "${svcName}-testing-${env.BUILD_NUMBER}"
  stage ('git'){
     checkout scm
  }
  def image = ''
  stage ('dockerize'){
	  image = docker.build "vygints/oto-${svcName}:${env.BUILD_NUMBER}"
  }
    
  stage ('push'){
      image.push()
  }
  def APP_URL=''
  stage ('deploy-to-testing'){
        sh "sed -i -- \'s/BUILD_NUMBER/${env.BUILD_NUMBER}/g\' ${svcName}-dep.yml"
        sh "kubectl create namespace ${nsName}"
        sh "kubectl apply -f mongodep.yml --validate=false -n ${nsName}"
        sh "kubectl apply -f ${svcName}-dep.yml --validate=false -n ${nsName}"
        //get app url
        APP_URL = "<pending>"
        sleep 120
        while ( APP_URL == "<pending>"){
            APP_URL = sh returnStdout: true, script: "kubectl get svc ${svcName} --no-headers=true  -n ${nsName} |  awk '{print \$3}'"
            APP_URL = APP_URL.trim()
            
        }
       
        echo "url is ${APP_URL}"
     }
    stage ('component-test'){
       withEnv(["APP_URL=${APP_URL}"]) {
	sh "tests/ct/run.sh"
       }
    }
    stage ('clean-up'){
	sh "kubectl delete ns ${nsName}"
    }
    stage('deply-to-staging'){
	sh "kubectl apply -f ${svcName}-dep.yml -n staging"  
    }
    stage ('integration-test'){
        echo "Not implemented"
    }
}
