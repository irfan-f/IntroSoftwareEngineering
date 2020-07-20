# Project 6: Brevet time calculator service

Simple listing service from project 5 stored in MongoDB database.

#Author
Irfan Filipovic
#Email
irfaf@uoregon.edu


# Implementation
A consumer program was added to port 5001 with the apis. To access program which displays buttons to test functionality access at http://0.0.0.0:5001/

The Brevet app has same functionalities as project 5 except the data is added to the database in a readable manner.

## Functionality you will add

This project has following four parts. Change the values for host and port according to your machine, and use the web browser to check the results.

* You will design RESTful service to expose what is stored in MongoDB. Specifically, you'll use the boilerplate given in DockerRestAPI folder, and create the following three basic APIs:
    * "http://<host:port>/listAll" should return all open and close times in the database
    * "http://<host:port>/listOpenOnly" should return open times only
    * "http://<host:port>/listCloseOnly" should return close times only

* You will also design two different representations: one in csv and one in json. For the above, JSON should be your default representation for the above three basic APIs. 
    * "http://<host:port>/listAll/csv" should return all open and close times in CSV format
    * "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
    * "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

    * "http://<host:port>/listAll/json" should return all open and close times in JSON format
    * "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
    * "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* You will also add a query parameter to get top "k" open and close times. For examples, see below.

    * "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
    * "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
    * "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
    * "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format

* You'll also design consumer programs (e.g., in jQuery) to use the service that you expose. "website" inside DockerRestAPI is an example of that. It is uses PHP. You're welcome to use either PHP or jQuery to consume your services. NOTE: your consumer program should be in a different container like example in DockerRestAPI.

## Tasks

You'll turn in your credentials.ini using which we will get the following:

* The working application with three parts.

* Dockerfile

* docker-compose.yml

## Grading Rubric

* If your code works as expected: 100 points. This includes:
    * Basic APIs work as expected.
    * Representations work as expected.
    * Query parameter-based APIs work as expected.
    * Consumer program works as expected. 

* For each non-working API, 5 points will be docked off. If none of them work,
  you'll get 35 points assuming
    * README is updated with your name and email ID.
    * The credentials.ini is submitted with the correct URL of your repo.
    * Dockerfile is present. 
    * Docker-compose.yml works/builds without any errors.

* If README is not updated, 5 points will be docked off. 

* If the Docker-compose.yml doesn't build or is missing, 15 points will be
  docked off. Same for Dockerfile as well.

* If credentials.ini is missing, 0 will be assigned.
