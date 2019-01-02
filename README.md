# Installation sur un Centos 7 vierge

# Configuration

``` bash
  yum -y upgrade
  yum install -y git
  yum install -y yum-utils device-mapper-persistent-data lvm2
  yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
  yum install -y docker-ce
  systemctl start docker
  systemctl enable docker
```

# Déploiement

``` bash
cd /;rm -rf hf18;mkdir hf18;cd hf18;git clone https://github.com/shawisec/Hackfest-MiniCTF-2018.git .;cd Scripts;chmod 700 *;./auto_deploy.sh
```
