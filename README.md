# Setps to run compose
## build web app image (from the app folder run)
bash build_docker_image.sh

## Update in docker-compose file
Edit docker-compose.yml (line 25) to point to existing path in your pc

## To run (from docker-compose folder)
docker-compose up -d

## To see logs (from docker-compose folder)
docker-compose logs -f

## To stop (from docker-compose folder)
docker-compose down

## Opens SwaggerUI and play with it
http://0.0.0.0/docs