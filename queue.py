class Queue:
	    def __init__(self):
	        self.items = []
	
	    def isEmpty(self):
	        return self.items == []
	
	    def enqueue(self, item):
	        self.items.insert(0,item)
	
	    def dequeue(self):
	        return self.items.pop()
	
	    def size(self):
	        return len(self.items)
	
q=Queue()
print 'is queue empty :', q.isEmpty()
q.enqueue('dog')
q.enqueue(4)
print 'elements in queue:', q.items
print 'Now is queue empty :',q.isEmpty()
q.enqueue(5)
q.enqueue(6)
print 'elements in queue:',q.items
print 'before dequeue size of the queue:',q.size()
q.dequeue()
q.dequeue()
q.dequeue()
print 'after dequeue size of the queue:',q.size()
print 'which elements left in queue:',q.items