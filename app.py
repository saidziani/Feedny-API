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

