# Project 4: Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax.

Credits to Michal Young for the initial version of this code.


Author: Irfan Filipovic

Email: irfanf@uoregon.edu

Repo: https://bitbucket.org/irfan-f/proj4-brevets

## ACP controle times

That's "controle" with an 'e', because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.   

The algorithm for calculating controle times is described here (https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here (https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly.  

We are essentially replacing the calculator here (https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data.  

## Calculator Implementation
Following the rules at https://rusa.org/pages/acp-brevet-control-times-calculator the calculator will take in the corresponding starting time, brevet distance, and the control last entered. Using the control it will calculate depending on its size whether in ranges (0,200), (200, 400), (400, 600), (600, 1000). At a control distance of 0 the open time is 00H:00M from the start, and the close is 01H:00M from the start.
When calculating the times using min and max speed, for each range it fufills the full km range. Therefore if the control distance is 201, 200 km are calculated in 0-200 range, and 1 in the 200-400. The same goes for each index change such as 401, 601...

Implementation for controls below 60 km has not been added to the project.


## Tasks

The code under "brevets" can serve as a starting point. It illustrates a very simple Ajax transaction between the Flask server and javascript on the web page. At present the server does not calculate times. It just returns double the number of miles. Other things may be missing; add them as needed. As before, you should fork and then clone the bitbucket repository, make your changes, and turn in the URL of your repository.

You'll turn in your credentials.ini using which we will get the following:

* The working application.

* A README.md file that includes not only identifying information (your name, email, etc.) but but also a revised, clear specification of the brevet controle time calculation rules.

* An automated 'nose' test suite.

* Dockerfile

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* AJAX in the frontend. That is, open and close times are automatically populated, 
	* Logic in the backend (acp_times.py), 
	* Frontend to backend interaction (with correct requests/responses), 
	* README is updated with a clear specification, and 
	* All five tests pass.

* If the AJAX logic is not working, 10 points will be docked off. 

* If the README is not clear or missing, up to 15 points will be docked off. 

* If the test cases fail, up to 15 points will be docked off. 

* If the logic in the acp_times.py file is wrong or is missing in the appropriate location, 30 points will be docked off.

* If none of the functionalities work, 30 points will be given assuming 
    * The credentials.ini is submitted with the correct URL of your repo, and
    * The Dockerfile builds without any errors
    
* If the Dockerfile doesn't build or is missing, 10 points will be docked off.

* If credentials.ini is missing, 0 will be assigned.
