# User App

Application based on Flaks and Angular to get users from https://reqres.in/api.
Whole front side is based on Angular and SASS preprocessor. Also whole project is in docker containers.

## Install:

There are few ways to install and test application:
1. Docker
2. Manual


#### Docker:
    1. Make shure you have docker installed
    2. docker-compose up -d
    3. docker exec users-app_backend_1 python -m unittest  # run test
    4. Open browser on localhost:8000 
    
#### Manual:
    1. Make shure you have nodejs>=10.0 installed
    2. Cloene repo
    3. Create an vitualenvironment via pyenv/virtualenv/conda etc.
    4. pip -r requirements.txt
    5. python -m unittest  # run test
    6. uwsgi --socket 0.0.0.0:5000 --protocol=http --module app:APP  # run backend
    5. cd static/src
    6. npm i
    7. npm i -g @angular/cli
    8. ng serve
    9. Open browser on localhost:4200 # run frontend
    
    
## Description:

#### Deployment:
I have put a project into docker container.
So it could be easily integrated with Cloud Systems such as AWS, Azure or Google Cloud.

Also there is Nginx as a proxy server.
Main purpose of that is to serving static files from frontend and pass all request to backend API.

#### Backend:
In the project I have made my own class NestableBlueprint to replace Flask Blueprint.
Unfortunately Flaks's blueprint cannot be nested, so I could not make a nested API.

The first blueprint is using for routing of API versions and thw second - for routing of app modules.

Also I have included there function **.register_view()** to register REST endpoint for whole MethodView (ViewSet in Django).
That is optional and you could add endpoint to your view via standard function **.add_url_rule()**.

Backend is serving through uWSGI that make code more secure. And in case if amount of requests would grow up - there is
 possible to create few workers to handle those requests.

#### Frontend:
For a frontend I have choice Angular mostly because I have more experience with that.
I think that React would be better for as small project as that. 
But otherwise it this project would grow up - Angular would be a better choice.


