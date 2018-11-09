docker swarm init

config_folder=/hf18/deploy/*
dirs=($(find $config_folder -type d))

for app in "${dirs[@]}";do
  filename="${app##*/}"
  docker stack deploy -c ${app}/docker-compose.yml ${filename}
  echo "imported: ${filename}"
done

docker pull owasp/modsecurity-crs

docker build -t owasp/modsecurity-crs ../Scoreboard/

docker run -p 80:80 -ti -e PARANOIA=5 --rm owasp/modsecurity-crs

docker service ls
