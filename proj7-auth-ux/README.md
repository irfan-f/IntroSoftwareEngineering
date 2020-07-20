# Project 7: Adding authentication and user interface to brevet time calculator service

Author: Irfan Filipovic
Project 7: CIS 322
Email: irfanf@uoregon.edu


References: A reference was used for CSRF protection, is listed within Auth/laptop/api.py


## Implemented Actions

** "http://0.0.0.0:5001/ui" :: Will bring you to a webpage where using links you can log in, log
   out get a token, register, and use test buttons for proj 6.

** "http://0.0.0.0:5001/register" :: Will bring you to registration.html to allow a user to be
    created for the username and  generated id, there is also a db entry created which contains
    the username, a hashed password, and the id. You will be redirected to 'api/ui' after submit
Register has the following form validator:
	Username cannot exist in db already, if it does red text will appear instructing so, and
        no user is created.

** "http://0.0.0.0:5001/login" :: Will allow you to login using a similar page to /register
    where you can enter username and password and submit to load_user using db id, and login.
    Has implemented remember_me functionality which is a checkbox on the log in page.
Log In has the following form validators:
	Username has to exist in the db already, if it does not red text will appear instructing
        so, and no user will be logged in.
        Password must match using verify_password(password, hash), if it does not red text will
        appear instructing so and no user will be logged in.


Both register and login are csrf protected in the .html files, and using CSRFPROTECT() in api.py.

** "http://0.0.0.0:5001/token" :: Will generate a token for the user, and will return the json
   object containing the token val, and the expiration time (600). Must be logged in to access,
   if not then will display message instructing so Token val must be accessed in order to access 
   the following endpoint:

** "http://0.0.0.0:5001/resources from proj 6" aka all buttons on "...:5001/" :: Must have
   Accessed token api first in order to access any information. As a fresh login the token will
   be wiped so access to the resources is not allowed. On failure a 401 should be displayed.


** "http://0.0.0.0:5001/logout" :: Will logout out the current user, but can only be accessed
   if logged in. If not logged in message will appear. On success will be redirected to /ui

** "http://0.0.0.0:5001/" :: Displays buttons from proj6, token protected


## Recap 

You will reuse *your* code from project 6 (https://bitbucket.org/UOCIS322/proj6-rest/). Recall: you created the following three parts: 

* You designed RESTful services to expose what is stored in MongoDB. Specifically, you used the boilerplate given in DockerRestAPI folder, and created the following:

** "http://<host:port>/listAll" should return all open and close times in the database

** "http://<host:port>/listOpenOnly" should return open times only

** "http://<host:port>/listCloseOnly" should return close times only

* You also designed two different representations: one in csv and one in json. For the above, JSON should be your default representation. 

** "http://<host:port>/listAll/csv" should return all open and close times in CSV format

** "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format

** "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

** "http://<host:port>/listAll/json" should return all open and close times in JSON format

** "http://<host:port>/listOpenOnly/json" should return open times only in JSON format

** "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* You also added a query parameter to get top "k" open and close times. For examples, see below.

** "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 

** "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format

* You'll also designed consumer programs (e.g., in jQuery) to expose the services.

## Functionality you will add

In this project, you will add the following functionality:

### Part 1: Authenticating the services 

- POST **/api/register**

Registers a new user. On success a status code 201 is returned. The body of the response contains a JSON object with the newly added user. A `Location` header contains the URI of the new user. On failure status code 400 (bad request) is returned. Note: The password is hashed before it is stored in the database. Once hashed, the original password is discarded. Your database should have three fields: id (unique index), username and password for storing the credentials.

- GET **/api/token**

Returns a token. This request must be authenticated using a HTTP Basic Authentication (see password.py for example). On success a JSON object is returned with a field `token` set to the authentication token for the user and a field `duration` set to the (approximate) number of seconds the token is valid. On failure status code 401 (unauthorized) is returned.

- GET **/RESOURCE-YOU-CREATED-IN-PROJECT-6**

Return a protected <resource>, which is basically what you created in project 6. This request must be authenticated using token-based authentication only (see testToken.py). HTTP password-based (basic) authentication is not allowed. On success a JSON object with data for the authenticated user is returned. On failure status code 401 (unauthorized) is returned.

### Part 2: User interface

The goal of this part of the project is to create frontend/UI for Brevet app using Flask-WTF and Flask-Login introduced in lectures. You frontend/UI should use the authentication that you created above. In addition to creating UI for basic authentication and token generation, you will add three additional functionalities in your UI: (a) remember me, (b) logout, and (c) CSRF protection. Note: You don’t have to maintain sessions.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
    * Basic APIs work as expected in part 1.
    * Decent user interface in part 2 including three functionalities in the UI.

* For each non-working API in part 1, 15 points will be docked off. Part 1 carries 45 points.

* For the UI and the three functionalies, decent UI carries 15 points. Each functionality carries 10 points. In short, part 2 carries 45 points.

* If none of them work, you'll get 10 points assuming
    * README is updated with your name and email ID.
    * The credentials.ini is submitted with the correct URL of your repo.
    * Dockerfile is present. 
    * Docker-compose.yml works/builds without any errors.

* If the Docker-compose.yml doesn't build or if credentials.ini is missing, 0 will be assigned.
