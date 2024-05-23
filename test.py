import queue_1

# Test the queue
myQueue = queue_1.Queue()

# Enqueue
myQueue.Enqueue('First job')
myQueue.Enqueue('Second job')
myQueue.Enqueue('Third job')

# Peek
print(myQueue.Peek())  # Should peek first job

# Dequeue
print(myQueue.Dequeue())  # should dequeue first job

# Enqueue
myQueue.Enqueue('Fourth job')

# Dequeue all
print(myQueue.Dequeue())
print(myQueue.Dequeue())
print(myQueue.Peek())

# Check if the queue is empty
print(myQueue.isEmpty()) 