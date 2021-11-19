docker-compose down
docker volume rm $(docker volume ls | grep blog | awk '{print $2}') 