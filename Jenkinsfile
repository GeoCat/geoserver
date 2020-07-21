import static groovy.io.FileType.FILES

pipeline {
    agent {
        docker {
            image 'maven:3.5.2-jdk-8'
        }
    }

    stages{
stage('BUILD') {
            steps {

                withEnv([
                    'HOME=.'
                ]) {
                    withMaven(
                        mavenSettingsConfig: 'nexusProxies') {
                        sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/pom.xml clean install -DskipTests -P${params.flavour}"
                    }
                }

            }
        }

        stage('WAR') {
            steps {

                withEnv([
                    'HOME=.'
                ]) {
                    withMaven(
                        mavenSettingsConfig: 'nexusProxies') {
                        sh "export PATH=$MVN_CMD_DIR:$PATH && mvn -f ./enterprise/webapp/pom.xml war:war -P${params.flavour}"
                    }
                }

            }
        }

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
    }
}