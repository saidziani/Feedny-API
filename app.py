from flask import Flask, jsonify, make_response, request, abort
from api_helper import ApiHelper

import sys
sys.path.insert(0,"../ArabicTextCategorization/lib/")
from helper import Helper 

app = Flask(__name__)
apiHelp = ApiHelper()
predictHelp = Helper()

articles = [
    {
        "title":"Why Starbucks faces toilet trouble",
        "summary":"Starbucks has amended its toilet policy to allow anyone to use the facilities - whether or not they purchase something - following a row over the treatment of black customers.",
        "content":"But the move by the US coffee chain could open the door to other problems including drugs, prostitution and homelessness."+
                "Starbucks chairman Howard Schultz announced on Thursday that the company's toilets would be available to anyone who asked."+
                "'We dont want to become a public bathroom, but were going to make the right decision 100% of the time and give people the key,' Mr Schultz told the Atlantic Council, a think tank in Washington DC."+
                "On 12 April, the manager at a Philadelphia Starbucks called the police on two black men who had requested to use the toilet without making a purchase. They were waiting for a business meeting and were arrested when they refused to leave."+
                "The subsequent outcry led to a settlement with the city and a public-relations disaster for Starbucks. The company apologised to the men and later this month will shut for one afternoon all 8,000 US stores as it holds mandatory anti-racial bias training for staff.",
        "image":"http://192.168.43.121/img/art1.jpg",
        "sourceName":"France 24",
        "sourceLogo":"http://192.168.43.121/img/bbc.png",
        "publishingTime":"1 hours ago",
        "author":"John Smith",
        "category":"politics"
    },
    {
        "title":"Burundi attack leaves 26 dead ahead of referendum",
        "summary":"At least 26 people were killed after armed attackers targeted a village in north-west Burundi, amid tensions ahead of a controversial referendum.",
        "content":"The group crossed from the Democratic Republic of Congo into Cibitoke province, officials said." +
        " They went house to house with guns and knives, burning homes, witnesses said." +
        "Correspondents say the attack may have been an attempt to disrupt next week's referendum which could extend the president's term until 2034."+
        "President Nkurunziza has ruled Burundi since the civil war ended there in 2005. His attempt to run for a third term in 2015 plunged the tiny central African nation into fresh turmoil.",
        "image":"http://192.168.43.121/img/art2.jpg",
        "sourceName":"BBC",
        "sourceLogo":"http://192.168.43.121/img/bbc.png",
        "publishingTime":"3 hours ago",
        "author":"Fouad Rkhila",
        "category":"society"
    },
    {
        "title":"PL boss provides the best value for money?",
        "summary":"It is easy to spend money in football. Spending it well is a lot harder.",
        "content":"At the very top, the sport is awash with spendthrift billionaire owners and ever-increasing television revenues leading to eye-watering transfer fees." +
        "To compete, it is imperative that the top clubs have thorough scouting, smart recruitment, intelligent coaching and, above all, a manager who can blend all of this into a successful side." +
        "Over the past two seasons, each of the Premier League's 'big six' - Arsenal, Chelsea, Liverpool, Manchester City, Manchester United and Tottenham - have kept their manager. But which have delivered the best return on their transfer outlay in that time.",
        "image":"http://192.168.43.121/img/art3.jpg",
        "sourceName":"AlJazeera",
        "sourceLogo":"http://192.168.43.121/img/bbc.png",
        "publishingTime":"5 minutes ago",
        "author":"Sebastien Courget",
        "category":"sports"
    },
    {
        "title":"Why Starbucks faces toilet trouble",
        "summary":"Starbucks has amended its toilet policy to allow anyone to use the facilities - whether or not they purchase something - following a row over the treatment of black customers.",
        "content":"But the move by the US coffee chain could open the door to other problems including drugs, prostitution and homelessness."+
                "Starbucks chairman Howard Schultz announced on Thursday that the company's toilets would be available to anyone who asked."+
                "'We dont want to become a public bathroom, but were going to make the right decision 100% of the time and give people the key,' Mr Schultz told the Atlantic Council, a think tank in Washington DC."+
                "On 12 April, the manager at a Philadelphia Starbucks called the police on two black men who had requested to use the toilet without making a purchase. They were waiting for a business meeting and were arrested when they refused to leave."+
                "The subsequent outcry led to a settlement with the city and a public-relations disaster for Starbucks. The company apologised to the men and later this month will shut for one afternoon all 8,000 US stores as it holds mandatory anti-racial bias training for staff.",
        "image":"http://192.168.43.121/img/art1.jpg",
        "sourceName":"France 24",
        "sourceLogo":"http://192.168.43.121/img/bbc.png",
        "publishingTime":"1 hours ago",
        "author":"John Smith",
        "category":"politics"
    },
    {
        "title":"Burundi attack leaves 26 dead ahead of referendum",
        "summary":"At least 26 people were killed after armed attackers targeted a village in north-west Burundi, amid tensions ahead of a controversial referendum.",
        "content":"The group crossed from the Democratic Republic of Congo into Cibitoke province, officials said." +
        " They went house to house with guns and knives, burning homes, witnesses said." +
        "Correspondents say the attack may have been an attempt to disrupt next week's referendum which could extend the president's term until 2034."+
        "President Nkurunziza has ruled Burundi since the civil war ended there in 2005. His attempt to run for a third term in 2015 plunged the tiny central African nation into fresh turmoil.",
        "image":"http://192.168.43.121/img/art2.jpg",
        "sourceName":"BBC",
        "sourceLogo":"http://192.168.43.121/img/bbc.png",
        "publishingTime":"3 hours ago",
        "author":"Fouad Rkhila",
        "category":"society"
    }
]

# Get category articles
@app.route('/api/articles/category=<category>', methods=['GET'])
# curl -i http://localhost:5000/api/articles/category=<category>
def getArticles(category):
    # articles = apiHelp.getArticlesByCategory("5af963201d41c81e212fbf1d")
    print(articles)
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

