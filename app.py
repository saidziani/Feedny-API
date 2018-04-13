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
