import settings
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

settings.init()

class DoorStatus(Resource):
    def get(self):
        return settings.doorStatus

    def post(self):
        data = request.get_json()
        if(int(data['status']) == 1):
            settings.doorStatus = "Door is Open"
        else:
            settings.doorStatus = "Door is Closed"
        return settings.doorStatus, 201

class MotionDetect(Resource):
    def get(self):
        return settings.motion

    def post(self):
        data = request.get_json()
        if data['motion'] == "1":
            settings.motion = "Motion Detected"
        elif data['motion'] == "0":
            settings.motion = "No motion detected"
        return settings.motion, 201

api.add_resource(DoorStatus, '/status_door')
api.add_resource(MotionDetect, '/motion_detect')

if __name__ == "__main__":
    app.run(port=5000)