class Stack:
    def __init__(self):
        self.counter = 0
        self.elements = []

    def push(self, value):
        self.elements.append(value)
        self.counter+=1

    def pull(self):
        if self.isEmpty():
            raise Stack.UnderFlow("You can't pull an empty stack")
        
        self.counter -=1 
        return self.elements[self.counter]
    
    def isEmpty(self):
        return self.counter == 0

    class UnderFlow(Exception):
        pass
