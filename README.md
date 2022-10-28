## BRADOO_Test



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
$ git clone https://github.com/JoaoNeto4/BRADOO_Test
```

### Navigate to the "api" folder
```
$ cd BRADOO_Test/api
```

### Start the containers
```
$ docker-compose up --build
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
http://localhost:8000/vendrs/
http://localhost:8000/products/
```





