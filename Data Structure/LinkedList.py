class Node:
    """
        demostrates a node that a linked list consists of

        Author
        ------
        Anim malvat
    """

    def __init__(self, value):
        """
            instantiates Node object

            Parameters
            ----------
            value: value of the node
        """

        self.data = value
        self.next = None

    def set_next(self, new_node):
        """
            sets next node's reference

            Parameters
            ----------
            new_node: node whose reference is to be added
        """

        self.next = new_node

    def get_next(self):
        """
            returns the next node

            Returns
            -------
            next: node that is in the next link
        """

        return self.next
    
    def get_data(self):
        """
            returns the data of the node

            Returns
            -------
            data: data of the node
        """
        return self.data

class LinkedList:
    """
        demonstrates a linked list

        Author
        ------
        Anim Malvat
    """

    def __init__(self):
        """
            instantiates the Linked list
        """

        self.head = None
    
    def add_in_head(self, value):
        """
            adds a node in head

            Parameters
            ----------
            value: value of the new node
        """

        if self.head == None:
            self.head = Node(value);
        else:
            new = Node(value)
            new.set_next(self.head)
            self.head = new
    
    def get_length(self):
        """
            generates length of the linked list

            Returns
            -------
            length: length of the linked list
        """
        node = self.head
        length = 0
        while node != None:
            length += 1
            node = node.get_next()
        return length

    def find(self, value):
        """
            finds element in the linked list

            Returns:
            boolean: true false according to the presence of the element
        """
        node = self.head

        while node != None:
            if node.get_data() == value:
                return True
            node = node.get_next()
        return False

    def __str__(self):
        """
            converts the linked list to string
        """

        result = "data: { "
        node = self.head
        while node != None:
            result += str(node.get_data())
            node = node.get_next()
            if node != None:
                result += ", "
        result += " }"
        return result

if __name__ == "__main__":
    list = LinkedList()
    list.add_in_head(2)
    list.add_in_head(3)
    list.add_in_head(4)

    print(f"length: {list.get_length()}")
    print(list)
    print(f'3 is in the list: {list.find(3)}')
    print(f'10 is in the list: {list.find(10)}')

