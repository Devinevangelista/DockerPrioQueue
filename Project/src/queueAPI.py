from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
import queue_1 as queue_1
import jobClass as jobClass

#initializes the fact we are using Flask API
app = Flask(__name__)
api = Api(app)

#initialize job queue
myJobQueue = queue_1.Queue()

#define job class
class JobResource(Resource):

    #seperate strings in file by commas
    def post(self):
        try:
            with open('input.txt', 'r') as file:
                for line in file:
                    uuid, taskName, priority = [item.strip() for item in line.split(',')]
                    newJob = jobClass.Job(uuid, taskName, int(priority))
                    myJobQueue.Enqueue(newJob)
            response = {"message": "Jobs from file added successfully"}
            return make_response(jsonify(response), 201)
        
        #exception handling for debugging
        except FileNotFoundError:
           response = {"message": "File not found"}
           return make_response(jsonify(response), 404)
        
        except Exception as e:
            response = {"message": str(e)}
            return make_response(jsonify(response), 500)

    def get(self):
        #get job at front of queue
        frontJob = myJobQueue.Peek()
        if frontJob:
            response = {"uuid": frontJob.id, "taskName": frontJob.taskName}
            return make_response(jsonify(response), 200)
        else:
            response = {"message": "No job in the queue"}
            return make_response(jsonify(response), 404)

class JobStatusResource(Resource):
    def get(self):
        #Get status of job queue
        status = myJobQueue.get_status()
        return make_response(jsonify(status), 200)
    
class JobRemoveResource(Resource):
    def delete(self, uuid):
        #remove job from queue by UUID
        if myJobQueue.DequeueByUUID(uuid):
            response = {"message": "Job removed"}
            return make_response(jsonify(response), 200)
        else:
            response = {"message": "Job not found"}
            return make_response(jsonify(response), 404)


api.add_resource(JobResource, '/jobs')
api.add_resource(JobStatusResource, '/jobs/status')
api.add_resource(JobRemoveResource, '/jobs/<string:uuid>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)