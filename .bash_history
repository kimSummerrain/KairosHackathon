mysql -u root
exit
ls
pwd
ls
exit
wget
wget https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.8.1%2B1/OpenJDK17U-jdk_x64_linux_hotspot_17.0.8.1_1.tar.gz
exit
ls
which java
ls /usr/local/
ls -l
tar xzf OpenJDK17U-jdk_x64_linux_hotspot_17.0.8.1_1.tar.gz -C /usr/local/
history 
ls -l /usr/local/
cat /etc/profile.d/openjdk.sh 
vi /etc/profile.d/openjdk.sh 
cat /etc/profile.d/openjdk.sh
ls
ls /etc/profile.d/
cat /etc/profile.d/tomcat9.sh 
vi /etc/profile.d/tomcat9.sh 
cat /etc/profile.d/tomcat9.sh 
cat /root/boot.sh 
source /etc/profile.d/openjdk.sh 
source /etc/profile.d/tomcat9.sh 
cd /usr/local/tomcat9/bin/
ls
./catalina.sh stop
pstree -uap
pstree -uap | less
netstat -natup
./catalina.sh start
netstat -natup
which java
java -version
ls
cd
pwd
wget https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.20.1%2B1/OpenJDK11U-jdk_x64_linux_hotspot_11.0.20.1_1.tar.gz
tar xzf OpenJDK11U-jdk_x64_linux_hotspot_11.0.20.1_1.tar.gz -C /usr/local/
ls /usr/local/
ls -l
rm OpenJDK1*
ls -l
df -h
netstat -natup
exit
date
locale
cd /etc/profile.d/
ls
cat lang.sh 
cd /root/boot.sh 
cd /root/
ls
cat boot.sh 
ls -l /etc/localtime 
ls -l /usr/share/zoneinfo/Asia/Seoul 
ls -l /etc/localtime 
ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
date
exit
ls
who
exit
git init
git add .
