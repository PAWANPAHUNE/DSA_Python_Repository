class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre = None

class DoublyLinkedList:
    def __init__(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp= self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
        self.length+=1

    def pop(self):
        if self.head == None:
            return None
        else:
            temp = self.tail
            self.tail = self.tail.pre
            self.tail.next = None
            temp.pre = None
            self.length-=1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp
        
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.head == None:
            return None
        temp = self.head
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next 
            self.head.pre = None 
            temp.next = None 
        self.length-=1
        return True
    
    def get(self,index):
        if index<0 or index>= self.length:
            return None
        if index<self.length/2:
            temp = self.head
            for _ in range (index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.pre
            return temp
        
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return False
        if index==0:
            self.prepend(value)
            return True
        if index==self.length:
            self.append(value)
            return True
        else :
            temp=self.get(index-1)
            after = temp.next
            temp.next = new_node
            new_node.pre = temp
            new_node.next = after
            after.pre = new_node
            self.length+=1
        
        return True
    
    def remove(self,index):
        temp = self.get(index)
        if temp==self.head:
            return self.pop_first()
        if temp==self.tail:
            return self.pop()
        if temp:
            before = temp.pre
            after = temp.next
            before.next = after
            after.pre = before 
            temp.next = None
            temp.pre = None
            self.length-=1
            return temp
        else:
            return False
        
    def reverse_between(self, start, end):
        if self.head is None or self.head.next is None:
            return False
        Dummy = Node(0)
        self.head.pre = Dummy
        Dummy.next = self.head
        pre = Dummy
        for i in range (start):
            pre = pre.next
        curr = pre.next
        for _ in range(end-start):
            to_move = curr.next
            pre.next = to_move
            to_move.pre = pre
            curr.next = to_move.next
            if curr.next is not None:
                curr.next.pre = curr
            to_move.next=pre.next
            curr.pre = to_move

            temp=pre
            print(f"it is {_}")
            while(temp):
                print(temp.value)
                temp=temp.next
            print("\n")


            
        self.head = Dummy.next
        self.head.pre = None
        self.print_list()
        print("\n")
            










        


        