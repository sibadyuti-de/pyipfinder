from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return jsonify({"ip": ip})
