from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import requests
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping():
    player_name = request.form['player_name']
    logging.info(f'Received ping from player: {player_name}')
    try:
        response = requests.post(
            'http://pong.app.kind.org:31080/pong',
            json={'player_name': player_name},
            timeout=5  # Optional timeout for the request
        )
        response.raise_for_status()  # Raise an error for bad responses
        logging.info(f'Received response from pong: {response.json()}')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        logging.error(f'Error during request: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
