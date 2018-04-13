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
