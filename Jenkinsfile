import static groovy.io.FileType.FILES

pipeline {
    agent {
        docker {
            image 'maven:3.5.2-jdk-8'
        }
    }

    stages{
    /*
        stage('INIT') {
            steps {
                sh "apt update && apt install ant"
            }
        }
        */
        stage('BUILD') {
            steps {
                withMaven(
                    mavenSettingsConfig: 'nexusProxies') {
                    sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/pom.xml clean install -DskipTests -Pstandard"
                }
            }
        }

        stage('WAR') {
            steps {
                withMaven(
                    mavenSettingsConfig: 'nexusProxies') {
                    sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/webapp/pom.xml war:war -Pstandard"
                }
            }
        }
        /*
        stage('DATA') {
            steps {

                withEnv([
                    'HOME=.'
                ]) {
                    withAnt() {
                        sh "ant -f ./data/build.xml default"
                    }
                }
            }
        }
        */
    /*
        stage('RELEASE') {
            environment {
                pom = readMavenPom file: './enterprise/pom.xml'
                version = pom.getVersion()
            }
            steps {
            
              withEnv([
                  'HOME=.' 
              ]) {
                   withMaven(mavenSettingsConfig: 'nexusProxies') {
                       sh "export PATH=$MVN_CMD_DIR:$PATH && mvn deploy:deploy-file -DartifactId=geoserver-enterprise-${params.flavour} -DgroupId=net.geocat.enterprise.geoserver -Dversion=${version} -Durl=https://nexus.geocat.net/repository/geoserver-geocat -DrepositoryId=nexus.proxy -Dfile=enterprise/webapp/target/geoserver-enterprise-${params.flavour}.war"
                   }
              }
            }
        }
    */
        stage ('Deploy to Development repo') {
            environment {
                ENTERPRISE_RELEASE = sh (script: 'mvn -f enterprise/pom.xml help:evaluate -Dexpression=geocat.enterprise -q -DforceStdout',returnStdout: true)
                NEXUS_URL = 'https://nexus.geocat.net/repository/enterprise-dev-releases'
            }

            steps {
                withCredentials([
                        string(credentialsId: 'geonetworkenterprise_basic_auth_token', 
                        variable: 'NEXUS_BASIC_AUTH')]) {

                    script {
                        def files = findFiles excludes: '', glob: 'enterprise/webapp/target/*.war'
                        def prefix = 'enterprise/webapp/target/'
                        
                        println "Staging ${files.size()} files for publishing"
                        
                        files.each { File file ->
                            println "pushing ${file}"
                            def sufix = file.getPath().substring(prefix.length())
                            
                            sh "curl -H \"Authorization: Basic ${NEXUS_BASIC_AUTH}\" --upload-file ./${file} ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geosever/${sufix}"
                        }
                    }
                    /*
                    script {
                        def files = findFiles excludes: '', glob: 'data/target/*.zip'
                        def prefix = 'data/target/'
                        
                        println "Staging ${files.size()} files for publishing"
                        
                        files.each { File file ->
                            println "pushing ${file}"
                            def sufix = file.getPath().substring(prefix.length())
                            
                            sh "curl -H \"Authorization: Basic ${NEXUS_BASIC_AUTH}\" --upload-file ./${file} ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geosever/${sufix}"
                        }
                    }
                    */
                }
            }
        }
        
        stage("Deploy to RELEASE repo") {
            when { buildingTag() }
            environment {
                ENTERPRISE_RELEASE = sh (script: 'mvn -f enterprise/pom.xml help:evaluate -Dexpression=geocat.enterprise -q -DforceStdout',returnStdout: true)
                NEXUS_URL = 'https://nexus.geocat.net/repository/enterprise'
            }
            steps {
                echo "This would deploy to RELEASE raw folder"
                withCredentials([
                        string(credentialsId: 'geonetworkenterprise_basic_auth_token', 
                        variable: 'NEXUS_BASIC_AUTH')]) {

                    script {
                        def files = findFiles excludes: '', glob: 'enterprise/webapp/target/*.war'
                        def prefix = 'enterprise/webapp/target/'
                                                
                        println "Staging ${files.size()} files for publishing"
                        
                        files.each { File file ->
                            println "pushing ${file}"
                            def sufix = file.getPath().substring(prefix.length())
                            
                            sh "curl -H \"Authorization: Basic ${NEXUS_BASIC_AUTH}\" --upload-file ./${file} ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geoserver/${sufix}"
                        }
                    }
                    /*
                    script {
                        def files = findFiles excludes: '', glob: 'data/target/*.zip'
                        def prefix = 'data/target/'
                        
                        println "Staging ${files.size()} files for publishing"
                        
                        files.each { File file ->
                            println "pushing ${file}"
                            def sufix = file.getPath().substring(prefix.length())
                            
                            sh "curl -H \"Authorization: Basic ${NEXUS_BASIC_AUTH}\" --upload-file ./${file} ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geosever/${sufix}"
                        }
                    }
                    */
                }
            }
        }
    }
}