from flask import Flask, jsonify, make_response, request, abort
from helper import Helper

app = Flask(__name__)
help = Helper()



# Get list of all articles
@app.route('/api/articles/category=<category>', methods=['GET'])
# curl -i http://localhost:5000/api/articles/category=<category>
def getArticles(category):
    articles = help.getArticlesByCategory(category)
    # print(articles)
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
    app.run(debug=True, host= '0.0.0.0')

