from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping():
    player_name = request.form['player_name']
    response = requests.post('http://pong.app.kind.org:31080/pong', json={'player_name': player_name})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
