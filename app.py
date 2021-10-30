from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

import Const
from WikiLeaks import WikiLeaksData

app = Flask(__name__)
api = Api(app)

params = reqparse.RequestParser()
params.add_argument("name", type=str, help='name is compulsory', required=True)
params.add_argument("id", type=int, help='id is compulsory')


class Topics(Resource):
    def get(self):
        return jsonify(WikiLeaksData().get_topics())


class Leaks(Resource):

    def get(self, top):
        return jsonify(WikiLeaksData().get_leaks(str(top)))


class FeatureLeaks(Resource):
    def get(self):
        return jsonify(WikiLeaksData().get_leaks(""))


api.add_resource(Topics, '/topic')
api.add_resource(Leaks, '/leaks/<string:top>')
api.add_resource(FeatureLeaks, '/top-leak')

if __name__ == "__main__":
    app.run(debug=True)
