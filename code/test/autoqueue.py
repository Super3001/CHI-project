# autoqueue.py

class AutoQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = []

    def enqueue(self, item:list):
        if len(self.queue) == self.maxsize:
            self.dequeue()
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def __str__(self):
        return str(self.queue)
    
    def average(self):
        x = sum([x[0] for x in self.queue]) / len(self.queue)
        y = sum([x[1] for x in self.queue]) / len(self.queue)
        z = sum([x[2] for x in self.queue]) / len(self.queue)
        return x,y,z
    