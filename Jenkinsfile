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
                sh "ant -f ./enterprise/data/build.xml download"
            }
        }

        stage('Build') {
            steps {
                withMaven(
                    mavenSettingsConfig: 'nexusProxies') {
                    println "Building requested 'community' modules not available online"
                    sh "export PATH=${MVN_CMD_DIR}:${PATH} && mvn -f ./geoserver/src/community/pom.xml -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn install -Pcog,geopkg,ogcapi -DskipTests"
                    println "Building GeoServer Enterprise"
                    sh "export PATH=${MVN_CMD_DIR}:${PATH} && mvn -f ./enterprise/pom.xml -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn install"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                withMaven(
                    mavenSettingsConfig: 'geocat.nexus.geoserver_enterprise') {
                    sh "export PATH=${MVN_CMD_DIR}:${PATH} && mvn -f ./enterprise/pom.xml -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn deploy"
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
                        def prefix = 'enterprise/webapp-*/target/'
                        def files = findFiles excludes: '', glob: prefix + '*.zip'
                        
                        println "Staging webapp ${files.size()} distribution bundles for publishing"
                        files.each { File file ->
                            println "Pushing ${file}"
                            def archive = file.getPath().substring(file.getPath().lastIndexOf('/')+1)
                            sh 'curl -H "Authorization: Basic ${NEXUS_BASIC_AUTH}" --upload-file ./' + "${file}" + ' ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geoserver/' + "${archive}"
                        }
                    }
                    script {
                        def prefix = 'enterprise/data/target/'
                        def files = findFiles excludes: '', glob: prefix + 'geoserver-data-*.zip'

                        println "Staging data ${files.size()} distribution bundles for publishing"
                        files.each { File file ->
                            println "Pushing ${file}"
                            def archive = file.getPath().substring(prefix.length())
                            sh 'curl -H "Authorization: Basic ${NEXUS_BASIC_AUTH}" --upload-file ./' + "${file}" + ' ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geoserver/' + "${archive}"
                        }
                    }
                }
            }
        }
        
        stage("Downloads (Release)") {
            when {
                allOf {
                    buildingTag()
                    not {
                        tag comparator: 'REGEXP', pattern: '(tags/live/.+)|(tags/.+-live)'
                    }
                }
            }
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
                        def prefix = 'enterprise/webapp-standard/target/'
                        def files = findFiles excludes: '', glob: prefix + '*.zip'
                        
                        println "Staging standard ${files.size()} distribution bundles for publishing"
                        files.each { File file ->
                            println "Pushing ${file}"
                            def archive = file.getPath().substring(prefix.length())
                            sh 'curl -H "Authorization: Basic ${NEXUS_BASIC_AUTH}" --upload-file ./' + "${file}" + ' ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geoserver/' + "${archive}"
                        }
                    }
                    script {
                        def prefix = 'enterprise/webapp-rws/target/'
                        def files = findFiles excludes: '', glob: prefix + '*.zip'
                        
                        println "Staging rws ${files.size()} distribution bundles for publishing"
                        files.each { File file ->
                            println "Pushing ${file}"
                            def archive = file.getPath().substring(prefix.length())
                            sh 'curl -H "Authorization: Basic ${NEXUS_BASIC_AUTH}" --upload-file ./' + "${file}" + ' ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geoserver/' + "${archive}"
                        }
                    }
                    script {
                        def prefix = 'enterprise/webapp-training/target/'
                        def files = findFiles excludes: '', glob: prefix + '*.zip'
                        
                        println "Staging training ${files.size()} distribution bundles for publishing"
                        files.each { File file ->
                            println "Pushing ${file}"
                            def archive = file.getPath().substring(prefix.length())
                            sh 'curl -H "Authorization: Basic ${NEXUS_BASIC_AUTH}" --upload-file ./' + "${file}" + ' ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geoserver/' + "${archive}"
                        }
                    }
                    script {
                        def prefix = 'enterprise/data/target/'
                        def files = findFiles excludes: '', glob: prefix + 'geoserver-data-*.zip'

                        println "Staging data ${files.size()} distribution bundles for publishing"
                        files.each { File file ->
                            println "Pushing ${file}"
                            def archive = file.getPath().substring(prefix.length())
                            sh 'curl -H "Authorization: Basic ${NEXUS_BASIC_AUTH}" --upload-file ./' + "${file}" + ' ${NEXUS_URL}/${ENTERPRISE_RELEASE}/geoserver/' + "${archive}"
                        }
                    }
                    
                }
            }
        }
        stage("Trigger live_gs job") {
            when {
                allOf {
                    buildingTag()
                    tag comparator: 'REGEXP', pattern: '(tags/live/.+)|(tags/.+-live)'
                }
            }
            
            steps{
                echo "Triggering Live Geoserver enterprise-2021-live image build job"
                build wait: false, job: '/live_gs/enterprise-2021-live', parameters: [string(name: 'argDataDir', value: '/usr/local/geoserver-live/data'), string(name: 'argRepository', value: 'enterprise-dev-releases')]
            }
        }
    }
}