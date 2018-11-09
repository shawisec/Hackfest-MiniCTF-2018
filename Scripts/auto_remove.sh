
config_folder=/hf18/deploy/*
dirs=($(find $config_folder -type d))

for app in "${dirs[@]}";do
  filename="${app##*/}"
  docker rm ${filename}
  echo "removed: ${filename}"
done

docker service ls

docker swarm leave --force
