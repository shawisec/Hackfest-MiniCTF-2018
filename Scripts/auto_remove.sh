config_folder=/hf18/deploy/*
dirs=($(find $config_folder -type d))

docker stop $(docker ps -aq)

for app in "${dirs[@]}";do
  filename="${app##*/}"
  id=(docker ps -aqf "name=${filename}")
  docker rmi ${id} --force
  echo "removed: ${filename}"
done

docker ps
