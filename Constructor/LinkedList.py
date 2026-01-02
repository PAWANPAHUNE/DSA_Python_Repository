class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self):
        temp= self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail=pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length :
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
    
    def partition_list(self,key):
        d1 = Node(value = 0)
        d2 = Node(value = 0)
        temp_1 = d1
        temp_2 = d2

        temp = self.head

        while(temp):
            if temp.value<key:
                temp_1.next = temp
                temp_1 = temp
            else:
                temp_2.next = temp
                temp_2 = temp

            temp = temp.next
        
        temp_2.next = None
        temp_1.next = d2.next
        self.head = d1.next
        return True
    
    def reverse_between(self,start,end):
        
        if self.length<=1:
            return True
            
        Dummy = Node(0)
        
            
        Dummy.next = self.head
        
        pre = Dummy
        
        for i in range(start):
            pre = pre.next
            
        curr = pre.next
        
        
        for _ in range(end-start):
            to_move = curr.next
            curr.next = to_move.next
            to_move.next = pre.next
            pre.next = to_move
            
        self.head = Dummy.next



