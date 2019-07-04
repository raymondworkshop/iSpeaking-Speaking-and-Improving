from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

@app.route('/record', methods=['GET', 'POST'])
def record():
    return

@app.route('/books', methods=['GET', 'POST'])
def books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS

    return jsonify(response_object)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong!')


#main
if __name__ == '__main__':
    app.run(debug=True)