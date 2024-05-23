import queue_1
import jobClass
import sys

#@description: reads in jobs from input file and stores them in a list of jobs 
#@param: filepath of inputFile 
#@return: jobs as a list of Job(object)
def readJobs(filePath):
    jobs = []
    myJob = jobClass.Job

    with open(filePath, 'r') as file:
        #reads input and puts in a list based on Job object type
        for line in file:
            id, taskName, priority = line.strip().split(",")
            job = myJob(id, taskName, int(priority))
            jobs.append(job)
        return jobs

#@description: processes jobs by queueing them in order and dequeuing as they are ran
#@param: filepath of inputFile
#@return: print statement to terminal of jobs ran
def processJobs(filePath):
    processQueue = queue_1.Queue()
    jobs = readJobs(filePath)

    for job in jobs:
        processQueue.Enqueue(job)

    while not processQueue.isEmpty():
        job = processQueue.Dequeue()    
        print(f"Running {job.taskName}")

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python main.py <jobs_file>")
        sys.exit
        
    jobsFile = sys.argv[1]
    processJobs(jobsFile)

