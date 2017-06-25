from flask import Flask, request
import services.events as events

app = Flask(__name__)

@app.route('/events/<type>', methods=['POST'])
def event(type):
    event = request.data


if __name__ == '__main__':
    app.run(host='0.0.0.0')