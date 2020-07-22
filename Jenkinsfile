import static groovy.io.FileType.FILES

pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build'
            dir 'buildtools'
        }
    }

    stages{

        stage('Data') {
            steps {
                sh "ant -f ./data/build.xml default"
            }
        }

        stage('Build') {
            steps {
                withMaven(
                    mavenSettingsConfig: 'nexusProxies') {
                    sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/pom.xml clean install -DskipTests"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                withMaven(
                    mavenSettingsConfig: 'geocat.nexus.geoserver_enterprise') {
                    sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/pom.xml deploy"
                }
            }
        }

        stage('WAR Bundles') {
            steps {
                withMaven(
                    mavenSettingsConfig: 'nexusProxies') {
                    sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/webapp/pom.xml war:war -Pstandard"
                }
                withMaven(
                    mavenSettingsConfig: 'nexusProxies') {
                    sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/webapp/pom.xml war:war -Plive"
                }
                withMaven(
                    mavenSettingsConfig: 'nexusProxies') {
                    sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/webapp/pom.xml war:war -Prws"
                }
            }
        }
        
        stage ('Downloads (Development)') {
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
                    
                }
            }
        }
        
        stage("Downloads (Release)") {
            when { buildingTag() }
            environment {
                ENTERPRISE_RELEASE = sh (script: 'mvn -f enterprise/pom.xml help:evaluate -Dexpression=geocat.enterprise -q -DforceStdout',returnStdout: true)
                NEXUS_URL = 'https://nexus.geocat.net/repository/enterprise'
            }
            steps {
                echo "This deploys to RELEASE raw folder"
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
                    
                }
            }
        }
    }
}