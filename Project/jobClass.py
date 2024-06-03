class Job:
    def __init__(self, uuid, taskName, priority, executionTime=30):
        self.id = uuid
        self.taskName = taskName
        self.priority = priority
        self.executionTime = executionTime

    def getRemainingTime(self):
        #placeholder  possibly implement remaining time calculation
        Time = " minutes"
        ConcatenatedTime  = (str(self.executionTime) + Time)
        return ConcatenatedTime

    def lessThan(self, other):
        return self.priority < other.priority
    
    #mainly used for testing and debugging
    def asAString(self):
        return f"Job(id={self.id}, taskName={self.taskName}, priority={self.priority})"