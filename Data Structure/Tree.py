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
        
    def pre_order(self):
        self.root.pre_order()

    def post_order(self):
        self.root.post_order()

    def in_order(self):
        self.root.in_order()



if __name__ == "__main__":
    tree = Tree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(4)
    tree.insert(2)
    print("tree in pre order: ")
    tree.pre_order()
    print("")
    print("tree in post order: ")
    tree.post_order()
    print("")
    print("tree in in order: ")
    tree.in_order()
    print("")
    print(f'5 is present in the tree: {tree.find(5)}')
    print(f'1 is present in the tree: {tree.find(1)}')
    
            
