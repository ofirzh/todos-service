#TODO-Service
This services implemented on top of [FastAPI](https://fastapi.tiangolo.com/) and
asynchronous mongodb connector [Motor](https://motor.readthedocs.io/en/stable/).
Service stores in MongoDB todos. Every saved in db todo holds "order" (priority) field.  
The order of todos is handled by sorting by this "priority" value. 
This approach has its side effects, but is simple enough. 

##Leftovers/Todos
-handle edge cases and add more statuses code.

-tune pydantic model and db model, to do less converting (ObjcetId and _id custom encoder)


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