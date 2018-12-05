#!/bin/bash
scoreboard_root_path=/hf18
deploy_path=/hf18/deploy

# Installation des dependances version CENTOS 7
yum install -y epel-release
yum install -y python-pip
pip install docker-compose
pip install --upgrade pip

#init le module swarn
docker swarm init

#Deploy CTFD Scoreboard
rm -rf ${scoreboard_root_path}/Scoreboard
mkdir -p ${scoreboard_root_path}/Scoreboard
cd ${scoreboard_root_path}/Scoreboard
git clone  https://github.com/mathieu244/CTFd.git .
docker-compose up

# Deploy all challenges
cd ${deploy_path}
for FILE in `ls -l`
do
    if test -d $FILE
    then
        docker stack deploy -c ${deploy_path}/${FILE}/docker-compose.yml ${FILE}
        echo "imported: ${FILE}"
    fi
done

docker service ls
