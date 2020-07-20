# Project 5: Brevet time calculator with Ajax and MongoDB

Simple list of controle times from project 4 stored in MongoDB database.

## Ambiguities
* Calculator has times set for each distance, 13.5 hours for 200, 20 for 300, 27 for 400, 40 for 600, 75 for 1000.

* Times above 200 get set at the next distance, and so on. So the range is 0-200, 201-400 .. etc

## Use

Entering a value into either miles or kms will prompt conversion to other type, and calculate open close times. Pressing submit will enter the data in a badly parsed string into MongoDB. Display button will open a new URL in which the data is presented.

## Button Tests

Submit Button
* No entries edge case, DO NOTHING
* Button clicked many times, only upload data once

Display Button
* No entries, display Nothing but open display page
* Button clicked many times, cannot occur


## COMMENTS

Currently the project uploads a very confusing string that contains all open and close times calculated and displays them as such. With further implementing the data could be displayed in a cleaner fashion, however the purpose of this assignment is to exhibit understanding of using mongodb and the other proccesses. Therefore with my lack of time i am leaving the strings as are.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* AJAX in the frontend. That is, open and close times are automatically populated, 
	* Frontend to backend interaction (with correct requests/responses), 
	* README is updated with your name and email.

* If the AJAX logic is not working, 10 points will be docked off. 

* If the README is not clear or missing, up to 15 points will be docked off. 

* If the two test cases fail, up to 15 points will be docked off. 

* If the logic to enter into or retrieve from the database is wrong, 30 points will be docked off.

* If none of the functionalities work, 30 points will be given assuming 
    * The credentials.ini is submitted with the correct URL of your repo, and
    * Dockerfile is present 
    * Docker-compose.yml works/builds without any errors 

* If the Docker-compose.yml doesn't build or is missing, 10 points will be docked off.

* If credentials.ini is missing, 0 will be assigned.
