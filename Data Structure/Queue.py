class Queue: 
    """
        queue data structure that supports First in First out
        @author Anim Malvat
    """
    def __init__(self, size = 5):
        """
            constructs the queue
            
            Parameters
            ----------
            size: size of the queue
        """
        self.head = -1
        self.tail = -1
        self.size = size
        self.data = [ 0 for i in range(self.size) ] # initializes data with 0 

    def isFull(self):
        """
            checks if the queue is full or not 

            Returns
            -------
            boolean: if full or not
        """
        if(self.head - 1 == self.tail or (self.head == 0 and self.tail == self.size - 1)):
            return True
        else:
            return False

    def isEmpty(self):
        """
            checks if the queue is empty or not

            Returns
            -------
            boolean: if empty or not
        """
        if(self.head == -1 and self.tail == -1):
            return True
        else:
            return False
    
    def insert(self, value):
        """
            inserts a value in the queue
        
            Parameters
            ----------
            value: value to be inserted
        """
        if(self.isFull()):
            return False
        else:
            if(self.head == -1):
                self.head = 0
                self.tail = 0
            else:
                if(self.tail == self.size - 1):
                    self.tail = 0
                else:
                    self.tail += 1
            self.data[self.tail] = value
        return True

    def delete(self):
        """
            deletes a value from the head 

            Returns
            -------
            value: value that is deleted
        """
        if(self.isEmpty()):
            return -1
        else:
            temp = 0
            if(self.head == self.tail):
                temp = self.data[self.head]
                self.head = -1
                self.tail = -1
            elif(self.head == self.size - 1):
                temp = self.data[self.head]
                self.head = 0
            else:
                temp = self.data[self.head]
                self.head += 1
            return temp
    
    def __str__(self):
        """
            prints the queue in readable format 

            Returns 
            -------
            String: readable format of queue
        """
        if(self.head == -1 and self.tail == -1):
            return "Error: Queue is empty"
        elif(self.head <= self.tail):
            result = "{"
            for i in range(self.head, self.tail):
                result += str(self.data[i]) + ", "
            result += str(self.data[self.tail]) + "}"
            return result
        else:
            result = "{"
            for i in range(self.head, self.size):
                result += str(self.data[i]) + ", "
            for i in range(self.tail):
                result += str(self.data[i]) + ", "
            result += str(self.data[self.tail]) + "}"
            return result

if(__name__ == "__main__"):
    q = Queue(3)
    print(q)
    print(f"inserting 1 : {q.insert(1)}")

    print(f"inserting 2 : {q.insert(2)}")

    print(f"inserting 3 : {q.insert(3)}")
    print(q)

    print(f"deleted : {q.delete()}")

    print(f"inserting 4 : {q.insert(4)}")

    print(q)
    print(f"deleted : {q.delete()}")
    print(f"deleted : {q.delete()}")
    print(q)
    print(f"deleted : {q.delete()}")

    print(q)
