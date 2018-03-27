import flask_restful as restful
from flask import Flask
from src.resources import FeatureRequestView


app = Flask(__name__)


restApi = restful.Api(app)
restApi.add_resource(FeatureRequestView, '/feature_request')


if __name__ == "__main__":
    app.run()
