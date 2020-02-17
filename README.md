# aws_exercise
Django Rest Framework application contenerizied in Docker

## To start the APP
    Open your terminal
    $ git clone https://github.com/bartoszbad/aws_exercise
    $ cd aws_exercise # Browse into the repo root directory
    To build Docker Image:
    $ docker build -f application_docker.Dockerfile -t <name_of_docker_image> .
    To run docker image and host application:
    $ docker run -it -p <number_of_port>:80 -d <name_of_docker_image>


## Endpoints:
```
<host>:<port>/echo (POST)
```
In case of json input returns:
{
“status”: “ok”,
“msg”: <text you posted>
}

In case of malformed json returns:
{
    "detail": "JSON parse error - Expecting value: line 1 column 1 (char 0)"
}

Because of DRF built in parser

```
<host>:<port>/random (GET)
```
returns: 
{
“status”: “ok”,
“number”: <some random number from 0 to 100>
}

## License:
Please see LICENSE file
