#!/bin/bash
scoreboard_root_path=/hf18
deploy_path=/hf18/deploy
challenge_path=/hf18/challenges
# Installation des dependances version CENTOS 7
yum install -y epel-release
yum install -y python-pip
pip install docker-compose
pip install --upgrade pip

#init le module swarn
#docker swarm init

#Deploy CTFD Scoreboard
rm -rf ${scoreboard_root_path}/Scoreboard
mkdir -p ${scoreboard_root_path}/Scoreboard
cd ${scoreboard_root_path}/Scoreboard
git clone  https://github.com/mathieu244/CTFd.git .
python -c "import os; f=open('.ctfd_secret_key', 'a+'); f.write(os.urandom(64)); f.close()"

cd ${scoreboard_root_path}/Scripts
python generate_flags.py
#copy le setup dans le scoreboard
mv shawisec.zip ${scoreboard_root_path}/Scoreboard/shawisec.zip

#cd ${scoreboard_root_path}/Scoreboard
docker-compose -f ${scoreboard_root_path}/Scoreboard/docker-compose.yml up -d
#docker stack deploy -c ${scoreboard_root_path}/Scoreboard/docker-compose.yml Scoreboard

# only for sql-1 challenge (reset database folder et donne les permission decriture pour apache)
rm -rf ${challenge_path}/sql-1/web/db;mkdir ${challenge_path}/sql-1/web/db;chmod -R 777 ${challenge_path}/sql-1/web/db; touch ${challenge_path}/sql-1/web/db/index.php;

# Deploy all challenges
cd ${deploy_path}
for FILE in `ls -l`
do
    if test -d $FILE
    then
        #docker stack deploy -c ${deploy_path}/${FILE}/docker-compose.yml ${FILE}
        docker-compose -f ${deploy_path}/${FILE}/docker-compose.yml up -d
        echo "imported: ${FILE}"
    fi
done

docker ps
