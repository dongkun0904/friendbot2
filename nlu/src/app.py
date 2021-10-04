from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from friendbot import Friendbot

app = Flask(__name__)
CORS(app)


# Create and train the friendbot
bot = Friendbot('Oppa')
bot.train()


@app.route('/nlu', methods=['POST'])
def friendbot():
    data = request.json
    if data is None:
        response = make_response(jsonify({'data': 'Data must exist'}), 400)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    if 'userInput' in data:
        userInput = data['userInput']
        print('user: {}'.format(userInput))
        botResponse = Friendbot.getBotResponse(userInput)
        print('bot: {}'.format(botResponse))
        response = make_response(jsonify({'data': botResponse.text}), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    response = make_response(jsonify({'data': 'Invalid data'}), 400)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5001, debug=True)
