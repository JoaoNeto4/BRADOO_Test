## BRADOO_Test


## Description
- Rest API project developed using Django, Django Framework and PostgreSQL, with the objective of evaluating technical skills.


## Prerequisites
```
$ sudo apt-get update
$ sudo apt-get install python3
$ sudo apt-get install docker
$ sudo apt-get install docker-compose
```

## Instructions

### Clone this repository
```
$ git clone https://github.com/JoaoNeto4/BRADOO_Test.git
```

### Navigate to the "api" folder
```
$ cd BRADOO_Test/api
```

### Start the containers
```
$ docker-compose up --build
```
> **Note**
> If there is some kind of permission error, run this:
```
$ sudo gpasswd -a $USER docker
$ newgrp docker
$ docker-compose up
```

### Run this line and copy the "ID" of the container "api_web"
```
$ docker ps
```

### Run this command with the "ID" from the previous step
```
$ docker exec -it <ID> bash
```

### Finally run the data migration
```
$ python manage.py makemigrations	
$ python manage.py migrate
```

### Now just access http://localhost:8000

### Valid endpoints
```
http://localhost:8000/vendors/
http://localhost:8000/products/
```





