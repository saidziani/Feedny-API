# Simple Flask API

All API access is over HTTP[S], and accessed from http://localhost:5000/api/people/. All data is sent and received as JSON.


### Data structure (json)

* Example of data 
    ```text
    {
        'id': 1,
        'name': 'Foo',
        'age': 25,
        'sexe': 'H',
        'student': False
    }
    ```


### Consuming API (curl)

* Get all rows: getPeople()
    ```text
    $ curl -i http://localhost:5000/api/people/
    ```


* Get one row using ID: getPerson(person_id)
    ```text
    $ curl -i http://localhost:5000/api/people/id=person_id
    ```


* Insert new row: createPerson()
    ```text
    $ curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Poo"}' http://localhost:5000/api/people/
    ```


* Update existing row using ID: updatePerson(person_id)
    ```text
    $ curl -i -H "Content-Type: application/json" -X PUT -d '{"student":true}' http://localhost:5000/api/people/id=2
    ```


* Delete existing row using ID: deletePerson(person_id)
    ```text
    $ curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/people/id=2
    ```


### Handle errors

*  Not found error (404)
    ```text
    HTTP/1.0 404 NOT FOUND
    {
        "error": "Not found"
    }
    ```

*  Bad  request error (400)
    ```text
    HTTP/1.0 400 BAD REQUEST
    {
        "error": "Bad request"
    }
    ```

