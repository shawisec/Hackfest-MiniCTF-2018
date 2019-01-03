config_folder=/hf18/deploy/*
dirs=($(find $config_folder -type d))

for app in "${dirs[@]}";do
  filename="${app##*/}"
  id=(docker ps -aqf "name=${filename}")
  docker stop ${id}
  echo "removed: ${filename}"
done

docker ps
