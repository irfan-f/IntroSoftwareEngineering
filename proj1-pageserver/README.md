# README #

A "getting started" project for CIS 322, introduction to software engineering, at the University of Oregon.

### What is this repository for? ###

The objectives of this mini-project are:

  * Experience with GIT workflow with separate configuration: Fork the project, make and test changes locally, commit; turn in configuration file with reference to repo. (Project 0 is practice for this part.) 
  * Extend a tiny web server in Python, to check understanding of basic web architecture
  * Use automated tests to check progress (plus manual tests for good measure)

### What do I need?  Where will it work? ###

* Designed for Unix, mostly interoperable on Linux (Ubuntu) or MacOS. May also work on Windows, but no promises. A Linux virtual machine may work, but our experience has not been good; you may want to test on shared server ix-dev.

* You will need Python version 3.4 or higher. 

* Designed to work in "user mode" (unprivileged), therefore using a port number above 1000 (rather than port 80 that a privileged web server would use)

* Windows 10 note: The new Windows bash on ubuntu looks promising. If you are running Windows 10, please give this a try and let me know if the Ubuntu/bash environment is suitable for CIS 322 develpment. 

### Assignment ###
* Fork this repository to create your own repository on Bitbucket. (Read the documentation as needed, and create an account on Bitbucket if you don't have one. You should've already done finished this as part of Project 0.) 
* Clone your repository onto the machine you want to work on.
* Add the following functionality in pageserver.py. (a) If URL ends with `name.html` or `name.css` (i.e., if `path/to/name.html` is in document path (from DOCROOT)), send content of `name.html` or `name.css` with proper http response. (b) If `name.html` is not in current directory Respond with 404 (not found). (c) If a page starts with one of the symbols(~ // ..), respond with 403 forbidden error. For example, `url=localhost:5000/..name.html` or `/~name.html` would give 403 forbidden error.
* Make and test your changes. Use both automated tests (the script in the 'tests' directory) and some manual tests.
* Revise this README.md file: Erase what is no longer relevant and add identifying information. If you have concerns about adding your email ID, let the instructors know.
  
  ```
  ## Author: Irfan Filipovic, irfanf@uoregon.edu #951603497
  ```

### Grading Rubric ###

* Your code works as expected: 100 points

* For every wrong functionality (i.e., (a), (b), and (c) above), 20 points will be docked off. 

* If none of the functionalities work, 40 points will be given. Assuming the credentials.ini is submitted with the correct URL of your repo.

* If credentials.ini is missing, 0 will be assigned.

### Who do I talk to? ###

* Maintained by Ram Durairajan, Steven Walton
* Use our Piazza group for questions. Make them public unless you have a good reason to make them private, so that everyone benefits from answers and discussion. 
