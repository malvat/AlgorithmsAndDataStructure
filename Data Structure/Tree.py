class Node:
    """
        node is a part of tree: tree is made up of several nodes

        Author
        ------
        Anim Malvat
    """
    def __init__(self, value):
        """
        instantiates Node object with value

        Parameter
        ---------
        value: value of the node
        """
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
            inserts a value to the node
            
            Parameter
            ---------
            value: value to be inserted at the node
        """
        if self.value == None:
            self.value = value
        else:
            if value > self.value:
                if self.right == None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
            else:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)

    def find(self, value):
        """
            find an element in the tree

            Parameter
            ---------
            value: value to be found
        """
        if self.value == value:
            return True
        else:
            if value > self.value:
                if self.right != None:
                    return self.right.find(value)
                else:
                    return False
            else:
                if self.left != None:
                    return self.left.find(value)
                else:
                    return False

    def pre_order(self):
        """
            prints the tree in pre-order traversal
        """
        print(self.value, end=" ")
        if self.left != None:
            self.left.pre_order()
        if self.right != None:
            self.right.pre_order()

    def post_order(self):
        """
            prints the tree in post-order traversal
        """
        if self.left != None:
            self.left.post_order()
        if self.right != None:
            self.right.post_order()
        print(self.value, end=" ")
    
    def in_order(self):
        """
            prints the tree in-order traversal
        """
        if self.left != None:
            self.left.in_order()
        print(self.value, end=" ")
        if self.right != None:
            self.right.in_order()


class Tree:
    """
        tree data structure that is non linear data structure
        
        Author
        ------
        Anim Malvat
    """
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def find(self, value):
        return self.root.find(value)
    
    def delete(self, value):
        """
            deletes the node from the tree with value given

            Parameter
            ---------
            value: value to be deleted
        """
        current = self.root         # set the current node to root
        parent = current            
        is_left_child = False       # to keep track if the current is parent's left child or right

        if current == None:
            # tree does not exists
            return False
        
        # traversing tree to find the node to be deleted
        while current != None and current.value != value:
            parent = current
            if value > current.value:
                is_left_child = False
                current = current.right
            else:
                is_left_child = True
                current = current.left
            if current == None:
                break
        
        if current == None:
            # element to be delete not found
            return False
        
        if current.left == None and current.right == None:
            print("no children")
            # if node has no children
            if is_left_child:
                parent.left = None
                return True
            else:
                parent.right = None
                return True
        elif current.left == None and current.right != None:
            print("left child")
            # if node has only right child
            if is_left_child:
                parent.left = current.right
            else:
                parent.right = current.left
        elif current.left != None and current.right == None:
            print("right child")
            # if node has only left child
            if is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            print("two children")
            # first we need to find current's right children's left most successor
            successor = current.right
            successor_parent = current
            while successor.left != None:
                successor_parent = sucessor
                successor = successor.left
            
            if is_left_child: 
                parent.left = successor
            else:
                parent.right = successor
            
            if successor == current.right:
                successor.left = current.left
            else:
                successor_parent.left = None
                successor.left = current.left
                successor.right = current.right



            
        

        
    def pre_order(self):
        self.root.pre_order()

    def post_order(self):
        self.root.post_order()

    def in_order(self):
        self.root.in_order()



if __name__ == "__main__":
    tree = Tree()
    tree.insert(50)
    tree.insert(70)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(15)
    tree.insert(25)
    print("tree in pre order: ")
    tree.pre_order()
    print("")
    print("tree in post order: ")
    tree.post_order()
    print("")
    print("tree in in order: ")
    tree.in_order()
    print("")
    print(f'5 is present in the tree: {tree.find(50)}')
    print(f'1 is present in the tree: {tree.find(10)}')
    print(f'20 is delete from the tree: {tree.delete(20)}')
    tree.in_order()
    
            
