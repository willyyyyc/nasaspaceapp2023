from flask import Flask, request

from swagger_server.controllers.default_controller import video_sonograph_post

app = Flask(__name__)

@app.route('/videoSonograph', methods=['POST'])
def hello_world():
    video_sonograph_post(request.json)

if __name__ == '__main__':
    app.run()