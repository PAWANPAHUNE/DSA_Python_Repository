class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class rBST:
    
    def __init__(self):
        self.root = None

    def __r_insert(self,current,value):
        if current == None:
            return Node(value)
        if value < current.value:
            current.left = self.__r_insert(current.left,value)
        if value > current.alue:
            current.right = self.__r_insert(current.right,value)

        return current.value

    def r_insert(self,value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root,value)
    
    def __r_contain(self,current_node,value):
        if current_node == None:
            return False
    
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contain(current_node.left,value)
        if value > current_node.value:
            return self.__r_contain(current_node.right,value)
        
    
    def r_contain(self,value):
        if self.root is None:
            return False
        return self.__r_contain(self.root,value)
    
    def min_subtree(self,current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
         
    def __r_delete(self,current_node,value):
        if current_node is None:
            return None
        if value<current_node.value:
            current_node.left = self.__r_delete(current_node.left,value)
        elif value>current_node.value:
            current_node.right = self.__r_delete(current_node.right,value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_min = self.min_subtree(current_node.right)
                current_node.value = sub_min
                current_node.right = self.__r_delete(current_node.right,sub_min)

        return current_node
    
    def delete_node(self,value):
        self.__r_delete(self.root,value)



        