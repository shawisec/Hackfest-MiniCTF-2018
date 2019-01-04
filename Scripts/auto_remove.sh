config_folder=/hf18/deploy/*
dirs=($(find $config_folder -type d))

docker stop $(docker ps -aq)
docker rmi $(docker images -aq)

echo "ALL REMOVED"

docker ps
