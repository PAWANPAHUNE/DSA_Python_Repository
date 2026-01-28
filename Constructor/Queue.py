class Node:
    def __init__(self,value):
        self.value = None
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.length==0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length+=1
    
    def dequeue(self):
        if self.first is None:
            return False
        

