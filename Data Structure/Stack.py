class Stack:
    """
        Stack data structure that supports first in last out
        @author Anim Malvat
    """
    def __init__(self, size = 5):
        """
            Parameters
            ----------
            size: size of the stack 
        """
        
        self.size = size
        self.data = [0 for i in range(self.size)]
        self.top = -1
    
    def isEmpty(self):
        """
            checks if the stack is empty or not

            Returns
            -------
            Boolean: condition of the stack (empty or not)
        """
        
        if self.top <= -1:  # -1 is the default value and hence means empty
            return True
        else: 
            return False
    
    def isFull(self):
        """
            checks if the stack is full or not

            Returns
            -------
            Boolean: condition of the stack (full or not)
        """

        if self.top + 1 >= self.size:
            return True
        else: 
            return False
    
    def push(self, value):
        """
            inserts value to the stack on top

            Parameters
            ----------
            value: value that is inserted in the stack
        """

        if not self.isFull():
            self.top += 1   # increment the top pointer
            self.data[self.top] = value
        else: 
            raise OverflowError

    def pop(self):
        """
            removes the top element from the stack

            Returns 
            -------
            Int: value that was present on the top (-1 on error)
        """

        if not self.isEmpty():
            temp = self.data[self.top]
            self.top -= 1   # decrement the top pointer
            return temp
        else: 
            raise OverflowError
        return -1
    
    def peep(self):
        """
            returns the top element without any operation

            Returns
            -------
            Int: value of top element
        """

        return self.data[self.top]
    
    def iter(self):
        """
            iterates like a stack
        """
        
        for i in range(self.top, -1, -1):
            yield self.data[i]

    def __str__(self):
        return f"Stack of size {self.size} filled upto {self.top + 1}"

def main():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("printing stack after pushing 1 2 and 3")
    for i in stack.iter():
        print(i)
    print(f"popped : {stack.pop()} ")
    print("printing stack after popping and pushing 4")
    stack.push(4)
    for i in stack.iter():
        print(i)
    print(f"printing top element {stack.peep()}")


if __name__ == "__main__":
    main()