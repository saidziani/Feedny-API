from flask import Flask, jsonify, make_response, request, abort

app = Flask(__name__)

articles = [
    {
        "article_id":1,
        "title":"Let's make America Great Again with Donald Trump",
        "summary":"je suii efnenl zfln zelfnlznglz USTHB zfuizfb zef",
        "content":"je suii efnenl zfln zelfnlznglz USTHB zfuizfb zef" +
        " je suii efnenl zfln zelfnlznglz USTHB zfuizfb zef " +
        "je suii efnenl zfln zelfnlznglz USTHB zfuizfb zef.",
        "image":"../assets/img/articles/1.jpg",
        "source":"France 24",
        "time":"Il y a 5 heures",
        "sourceImage":"../assets/img/articles/2.jpg"
    },
]

# Get list of all people
@app.route('/api/articles/', methods=['GET'])
# curl -i http://localhost:5000/api/people/
def getPeople():
    if len(articles) == 0:
        abort(404)
    return jsonify({'articles': articles})


# Error handling
@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def badRequest(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
    app.run(debug=True)

