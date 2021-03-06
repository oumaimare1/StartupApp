# Deployment of Machine Learning model on Heroku using Docker and RestAPI

In this project, a multiple regression model is deployed on Heroku using Docker and Flask API.
<p align="center">
<img src="https://user-images.githubusercontent.com/77075553/104852589-2aeb5200-58fc-11eb-9cb7-8bbc559eae8c.jpeg" width="600">
</p>

## Table of contents : 
- [General Info](#general-info)
  * [Project Steps](#project-steps--)
  * [Docker](#docker)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Part 1 - Create A Basic Flask App](#part-1---create-a-basic-flask-app)
- [Part 2 - Dockerize the Application](#part-2---dockerize-the-application)
- [Part 3 - Deploy the Application to Heroku](#part-3---deploy-the-application-to-heroku)
- [The Heroku App](#the-heroku-app)



## General Info 
The model created is used to predict a startups profit using Multiple Linear Regression in Python. The dataset used contains the details of 50 startups and predicts the profit of a new Startup based on certain features. I will deploy this model on Heroku using Flask and Docker.

### Docker : 
Docker is a containerization service that allows for websites, APIs, databases, and, in our case, data science models to be deployed anywhere and ran with a few to only one line of code.
Docker is lightweight and doesn't take up as much memory as other methods and has a faster startup time. Allowing you to easily update your models and test and deploy the changes quickly.

### Project Steps : 
* Part 1 -  Train and save the model & Create A Flask App
* Part 2 - Dockerize the Application
* Part 3 - Deploy the Application to Heroku

<p align="center">
<img src="https://user-images.githubusercontent.com/77075553/104852592-2d4dac00-58fc-11eb-8c42-555e975045af.png" width="400">
</p>


## Prerequisites
* [Docker](https://www.docker.com/)
* [Scikit Learn](https://scikit-learn.org/stable/)
* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
 
## Project Structure
This project has four major parts :
1. model.py - Contains the code of our machine learning model to predict the profit of startups based on data data "50_Startup.csv".
2. app.py - Contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates & static - This folders contains the HTML & CSS templates to allow user to enter employee detail and displays the predicted startup profit.

## Part 1 - Create A Basic Flask App
Create an API to send data and make predictions with my model

1. Clone this repo to your desktop, and install all the dependencies : 
```
install -r requirements.txt
```
2. Create the machine learning model by running below command - This would create a serialized version of our model into a file model.pkl
```
python model.py
```

3. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on http://0.0.0.0:5000/ (localhost)

## Part 2 - Dockerize the Application
Create a Dockerfile specified to my model and it’s requirements.

1. Enter the command to create the Docker image from the file Dockerfile : 
```
docker image build -t docker-startup .
```
2. Launch the built image into the container with the command :
```
docker run -p 5000 -d docker-startup
```

## Part 3 - Deploy the Application to Heroku

1. Create a Heroku app using the command : 
```
heroku create startup-profit-app
```
2. Create a heroku.yml file : 

We need to create a heroku.yml file, so we can deploy our image docker on Heroku. 
This is a new 'file manifest' that can be used to define the build.

It includes 2 sections to specify how an application should be created and run.

3. Change the Heroku stack by default and set the stack container : 
```
heroku stack:set container --app startup-profit-app 
```
4. Once we've set up the app, we'll deploy it to Github by associating it with Heroku.
![alt text](https://user-images.githubusercontent.com/77075553/104853966-96392200-5904-11eb-9950-63b9f2ab71e5.png)

![alt text](https://user-images.githubusercontent.com/77075553/104853967-96d1b880-5904-11eb-9aa6-55f15cc54942.png)

## The Heroku App 
Here is the link to the Heroku app : 
https://startup-profit.herokuapp.com/
