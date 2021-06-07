Quick start:
```
$ git clone https://github.com/federicodv/obj_test.git && docker-compose -f obj_test/docker-compose.yml up --build
```

To deploy:  
docker-compose up --build  

Test if everithing is working ok:  
```shell
$ curl http://127.0.0.1:5000  
```
you have to see a "hello world" response  

GraphQL test endpoint:  
http://127.0.0.1:5000/object


Run tests:
```shell
$ docker exec -it obj-api pytest 
```

Quick description of the solution:
When the flask app start  a data.json file is created with a list of ints (1 to 10 by default)

To get an object (see **GraphQL test endpoint**):
```
 { get_object{ obj }}
```
The object will be removed from the data.json objects list

To free an object (see **GraphQL test endpoint**):
```
 { free_object(obj:999){ obj }}
```
The object will be added to the data.json objects list

List current items:
```
{
  list_objects {
    obj
  }
}
```

