from flask import Flask, request
from redis import Redis

app = Flask(__name__)

redis = Redis(host='redis', port=6379)
redis.set('name', 'Hello World')

@app.route('/project')
def project_endpoint():
    return redis.get('name')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
