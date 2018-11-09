#!/bin/bash
challenge_path=/hf18/challenges
deploy_path=/hf18/deploy


#init le module swarn
docker swarm init

#copie le scoreboard dans le repertoire des challenges
rm -rf $challenge_path/Scoreboard
mkdir -p $challenge_path/Scoreboard
cd challenge_path/Scoreboard
git clone  https://github.com/mathieu244/CTFd.git .

#copie le docker-composer dans le repertoire de deploiement
rm -rf $deploy_path/Scoreboard
mkdir -p $deploy_path/Scoreboard
cp $challenge_path/Scoreboard/docker-composer.yml $deploy_path/Scoreboard

cd ${config_folder}
for FILE in `ls -l`
do
    if test -d $FILE
    then
        docker stack deploy -c ${config_folder}/${FILE}/docker-compose.yml ${FILE}
        echo "imported: ${FILE}"
    fi
done

docker service ls
