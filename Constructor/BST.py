class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if temp.value==new_node.value:
                return False
            if temp.value>new_node.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right 

    def contain(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif temp.value>value:
                temp = temp.left
            else:
                temp = temp.right

        return False
    
    def min_value(self,current_node):
        while current_node:
            current_node = current_node.left
        current_node.value

        



        

        
         



