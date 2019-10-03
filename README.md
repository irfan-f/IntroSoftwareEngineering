# Proj0-Hello
-------------

Trivial project to exercise version control, turn-in, and other
mechanisms.

# Information:
--------------

Author: Irfan Filipovic
Date: 10/03/2019
Email: irfanf@uoregon.edu

# Description:
--------------

The file hello.py will access the message data located in the credentials file, and print the string to the console.


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
    $ sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common
    ```

3. Add Docker's official GPG key:

    ```
    $ curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -
    ```

    Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

    ```
    $ sudo apt-key fingerprint 0EBFCD88
    ```

4. Setup stable repository:

    ```
    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"
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
