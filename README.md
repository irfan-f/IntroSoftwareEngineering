# Proj0-Hello
=============
Trivial project to exercise version control, turn-in, and other
mechanisms.

## Instructions:
---------------

- Start by forking this repository on [bitbucket](https://bitbucket.org/UOCIS322/proj0-hello), then cloning onto your
  development machine. Read this file (README.md). 
  
- Before you edit a file, read the comments (inside that file) carefully.

- Copy the credentials-skel.ini file to credentials.ini and fill in
  appropriately.

- Modify the program "hello.py" so that it prints "Hello
  world". (Nothing more and nothing less.)  Note that you do NOT do
  this by changing the hello.py source file. Rather, the message is a
  configuration constant from the credentials.ini file; fix it there.

- Replace these instructions with a proper README including the
   author, contact address, and a brief description of what the
   software does.

- Test your program locally;  revise and re-test as needed.  (How long
  can it take, really?)

- Commit your changes. You will need to use "git add" on your files
   hello.py and README.md, but *not* on credentials.py, because that
   file does not belong on bitbucket.  (In later projects it will contain
   confidential information, like access keys and passwords for web
   services.)  Your changes must be "pushed" to your public repository
   on bitbucket so that the auto-checker can "clone" them back to the
   grading machine.

- Test your code with the auto-checker. Revise and push changes
   as needed.

- Turn in with Canvas. The file you turn in is credentials.ini. We
   use the repository link in your credentials.ini to access the rest,
   just like the auto-checker.

# Docker Setup
-------------
The following instructions are provided for Linux users.
Make sure that you have a reasonably recent version.
The snippets are to be pasted in your terminal( Without '$' sign).
If you are [Mac](https://docs.docker.com/docker-for-mac/install/) or a
[Windows](https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows)
user, follow the instructions from the respective link provided. It should be straightforward.

1. Update apt package:

    ```
    $ sudo apt update
    ```

2. Install packages to allow apt to use a repository over HTTPS:

    ```
    $ sudo apt install \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg2 \
      software-properties-common
    ```

3. Add Docker’s official GPG key:

    ```
    $ curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -
    ```
  Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

    ```
  $ sudo apt-key fingerprint 0EBFCD88
    ```

4. Setup stable repository:

    ```
    $ sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
      $(lsb_release -cs) \
      stable"
    ```

5. Install DOCKER CE:

    ```
    $ sudo apt install docker-ce
    ```

6. Verify that Docker CE is installed correctly by running the hello-world image.

    ```
    $ sudo docker run hello-world
    ```

This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits. For more information: (https://docs.docker.com/get-started/)
