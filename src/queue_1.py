import src.jobClass as jobClass

class Node(object):
    #self refers to node, data is inside the node
    def __init__(self, data):
        #set data
        self.data = data 
        self.next = None

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None
    
    def Peek(self):
        #Handle empty queue case
        if self.isEmpty():
                return None
        return self.head.data
        
    def Enqueue(self, data):
        newNode = Node(data)
        #If the queue is empty, value should become head node
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            #If new node has higher prio than head, insert new node before head, update head
            if self.head.data.priority > data.priority:
                newNode.next = self.head
                self.head = newNode
            else:
            #Find correct position in queue to insert new node
                current = self.head
                #traverse queue to find position where the new node should be inserted
                while current.next is not None and current.next.data.priority <= data.priority:
                    current = current.next
                newNode.next = current.next
                current.next = newNode
                if newNode.next is None:
                    self.tail = newNode

    def Dequeue(self):
        #Handle empty queue case
        if self.isEmpty():
            return None 
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        return data
    
    