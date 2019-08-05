# FantasyWebApp

A basic web app to get useful information about fantasy basketball during game weeks. Visit the live website [here](https://fantasytool.herokuapp.com).


## Running Through Docker 
Make sure to install [Docker](https://docs.docker.com/install/) and required dependencies.
 * Open up a command prompt 
 * Navigate to the directory where the Dockerfile and docker-compose.yml are located 
 * Run the `docker-compose up` command 
 * Open up a web browser and go to `192.168.99.100:8000`
 
## Running Locally 
 * Clone directory 
 * Install required modules listed with `pip install -r requirements.txt`
 * Navigate to the directory where `manage.py` is located 
 * Run the command `python manage.py runserver`
 * Open up a web browser and go to `localhost:8000`
