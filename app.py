from flask import Flask

app = Flask(__name__)

people = [
    {
        'id': 1,
        'name': 'Foo',
        'age': 25,
        'sexe': 'H',
        'student': False
    },
    {
        'id': 2,
        'name': 'Boo',
        'age': 22,
        'sexe': 'F',
        'student': True
    }
]

# Get list of all people
@app.route('/api/people/', methods=['GET'])
# curl -i http://localhost:5000/api/people/
def getPeople():
    if len(people) == 0:
        abort(404)
    return jsonify({'people': people})

	
# Get one person by id
@app.route('/api/people/id=<int:person_id>', methods=['GET'])
# curl -i http://localhost:5000/api/people/id=2
def getPerson(person_id):
    person = [person for person in people if person['id'] == person_id]
    if len(person) == 0:
        notFound(abort(404))
    return jsonify({'person': person})


# Create new person <name> required
@app.route('/api/people/', methods=['POST'])
# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Poo"}' http://localhost:5000/api/people/
def createPerson():
    if not request.json or not 'name' in request.json:
        badRequest(abort(400))
    person = {
        'id': people[-1]['id'] + 1,
        'name': request.json['name'],
        'age': request.json.get('age', 0),
        'sexe': request.json.get('sexe', ''),
        'student': False
    }
    people.append(person)
    return jsonify({'person': person}), 201


# Update existing person
@app.route('/api/people/id=<int:person_id>', methods=['PUT'])
# curl -i -H "Content-Type: application/json" -X PUT -d '{"student":true}' http://localhost:5000/api/people/id=2
def update_task(person_id):
    person = [person for person in people if person['id'] == person_id]
    if len(person) == 0:
        notFound(abort(404))
    if not request.json:
        badRequest(abort(400))
    if 'name' in request.json and type(request.json['name']) is not str:
        badRequest(abort(400))
    if 'age' in request.json and type(request.json['age']) is not int:
        badRequest(abort(400))
    if 'sexe' in request.json and type(request.json['sexe']) is not str:
        badRequest(abort(400))
    if 'student' in request.json and type(request.json['student']) is not bool:
        badRequest(abort(400))
    person[0]['name'] = request.json.get('name', person[0]['name'])
    person[0]['age'] = request.json.get('age', person[0]['age'])
    person[0]['sexe'] = request.json.get('sexe', person[0]['sexe'])
    person[0]['student'] = request.json.get('student', person[0]['student'])
    return jsonify({'person': person})



# Delete existing person
@app.route('/api/people/id=<int:person_id>', methods=['DELETE'])
# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/people/id=2
def deletePerson(person_id):
    person = [person for person in people if person['id'] == person_id]
    if len(person) == 0:
        notFound(abort(404))
    people.remove(person[0])
    return jsonify({'result': True})

