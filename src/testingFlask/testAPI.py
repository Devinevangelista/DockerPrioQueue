from flask import Flask
from flask_restful import Api, Resource

#initializes the fact we are using Flask API
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    #what will happen when get request is sent to url
    def get(self, name):
        #everytime we return information, we want it to be serialized, represents json format
        return {"data": name}
    
    def post(self):
        return {"data": "Posted"}

##should return helloworld when called
api.add_resource(HelloWorld, "/helloworld/<string:name>")

#will start our server/flask app in debug mode. Don't use in production env
if __name__ == "__main__":
    app.run(debug=True)
