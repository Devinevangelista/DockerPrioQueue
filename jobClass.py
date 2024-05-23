
class Job:
    def __init__(self, uuid, taskName, priority):
        self.id = uuid
        self.taskName = taskName
        self.priority = priority

    def lessThan(self, other):
        return self.priority < other.priority
    
    #mainly used for testing and debugging
    def asAString(self):
        return f"Job(id={self.id}, taskName={self.taskName}, priority={self.priority})"