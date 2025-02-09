from flask import Flask, request, jsonify
import os
import redis
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/pong', methods=['POST'])
def pong():
    data = request.json
    player_name = data.get('player_name', 'unknown')
    count = redis_client.incr(player_name)
    redis_client.expire(player_name, 60)  # Set TTL to 1 minute
    pod_name = os.getenv('POD_NAME', 'unknown')
    logging.info(f'Pong received from player: {player_name}, count: {count}, pod: {pod_name}')
    return jsonify({'player_name': player_name, 'count': count, 'pod_name': pod_name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
