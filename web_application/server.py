from flask import Flask
from flask import send_file
import web_application.service.elasticsearch as es_service

app = Flask(__name__)


@app.route('/get_file/<file>')
def get_file(file):
    return send_file(file)


@app.route('/map/<track>')
def send_js(track):
    return send_file('teste.html')


@app.route('/find_track/<track>')
def find_track(track):
    return es_service.retrieve_by_id(track)


if __name__ == "__main__":
    app.run(debug=True)
