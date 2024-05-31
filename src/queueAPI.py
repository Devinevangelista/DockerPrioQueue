from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import queue_1 as queue_1
import jobClass as jobClass
import io

#initializes the fact we are using Flask API
app = Flask(__name__)
api = Api(app)

#initialize job queue
myJobQueue = jobClass.queue()

#define job class
class JobResource(Resource):
    def post(self):

        if 'file' not in request.files:
            return jsonify({"message": "No file part in the request"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "No file selected for uploading"}), 400

        #add job to queue, set 
        dataRequest = request.get_json()
        uuid = dataRequest.get('uuid')
        taskName = dataRequest.get('taskName')
        priority = dataRequest.get('priority')

        newJob = jobClass.Job(uuid, taskName, priority)
        myJobQueue.Enqueue(newJob)
        return jsonify({"message": "Job added successfully"}), 201

    def get(self):
        #get job at front of queue
        frontJob = myJobQueue.Peek()
        if frontJob:
            return jsonify({"uuid": frontJob.id, "taskName": frontJob.taskName}), 200
        else:
            return jsonify({"message": "No job in the queue"}), 404

class JobStatusResource(Resource):
    def get(self):
        #Get status of job queue
        status = [{"uuid": job.uuid, "taskName": job.taskName, "priority": job.priority} for job in myJobQueue.get_status()]
        return jsonify(status), 200
    
class JobRemoveResource(Resource):
    def delete(self, uuid):
        #remove job from queue by UUID
        if myJobQueue.Dequeue(uuid):
            return jsonify({"message": "Job removed"}), 200
        else:
            return jsonify({"message": "Job not found"}), 404
        

