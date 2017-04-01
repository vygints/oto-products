node ('slave1'){
    stage ('git'){
       checkout scm
    }
  
   def image = ''
   stage ('dockerize'){
       image = docker.build "otomato/oto-products:${env.BUILD_NUMBER}"
   }
    
    
    stage ('push'){
        image.push()
    }
    stage ('deploy'){
         sh 'kubectl apply -f products-dep.yml --validate=false'
     }

}
