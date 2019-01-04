config_folder=/hf18/deploy/*
dirs=($(find $config_folder -type d))

docker kill $(docker ps -q)
docker stop $(docker ps -aq)

docker rmi $(docker images -aq) --force

echo "ALL REMOVED"

docker ps
