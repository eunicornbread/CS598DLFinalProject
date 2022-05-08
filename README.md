docker build -t spark_docker . 
navigate to folder mimic-on-spark
(in cmd, in other terminals, need to replace %cd% with the absolute path) docker run -it -v %cd%:/my_repo spark_docker bin/bash


in the docker container
cd my_repo/
install gradle in container
follow this link: https://linuxize.com/post/how-to-install-gradle-on-ubuntu-18-04/

wget https://services.gradle.org/distributions/gradle-5.0-bin.zip -P /tmp
sudo unzip -d /opt/gradle /tmp/gradle-*.zip
ls /opt/gradle/gradle-5.0

vim /etc/profile.d/gradle.sh

paste the following code:
export GRADLE_HOME=/opt/gradle/gradle-5.0
export PATH=${GRADLE_HOME}/bin:${PATH}

sudo chmod +x /etc/profile.d/gradle.sh
source /etc/profile.d/gradle.sh

<!-- verify Gradle is installed properly -->
gradle -v
<!-- output -->
Welcome to Gradle 5.0!

Here are the highlights of this release:
 - Kotlin DSL 1.0
 - Task timeouts
 - Dependency alignment aka BOM support
 - Interactive `gradle init`

For more details see https://docs.gradle.org/5.0/release-notes.html


------------------------------------------------------------
Gradle 5.0
------------------------------------------------------------

Build time:   2018-11-26 11:48:43 UTC
Revision:     7fc6e5abf2fc5fe0824aec8a0f5462664dbcd987

Kotlin DSL:   1.0.4
Kotlin:       1.3.10
Groovy:       2.5.4
Ant:          Apache Ant(TM) version 1.9.13 compiled on July 10 2018
JVM:          1.8.0_312 (Private Build 25.312-b07)
OS:           Linux 5.4.72-microsoft-standard-WSL2 amd64



<!-- add the gradle wrapper -->
gradle wrapper
<!-- output -->
Starting a Gradle Daemon (subsequent builds will be faster)

BUILD SUCCESSFUL in 4s
1 actionable task: 1 executed

<!-- now we can compile following the repo instruction -->
./gradlew jar

put csv files in a data folder

replace build.gradle file and gradle-wreapper.properties file since the original ones are outdated and will prevent compiling