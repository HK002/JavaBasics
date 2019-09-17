class Node:
    def __init__(self,data):
        self.value = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self,data):
        if self.start is None:
            self.start = Node(data)
        else:
            x = self.start
            while x.link is not None:
                x = x.link
            x.link = Node(data)    

    def display(self):
        if self.start is None:
            print("List is Empty")
        else:
            x=self.start
            while x is not None:
                print(x.value, end = " ")
                x = x.link    

    def middleElement(self):
        if self.start is None :
            print("Empty List")
        else:
            spointer = self.start
            fpointer = self.start
            while fpointer is not None and fpointer.link is not None:
                spointer = spointer.link
                fpointer = fpointer.link.link
            print("\nMiddle Element : " + str(spointer.value))    



obj=LinkedList()
obj.insert(1)
obj.insert(2)
obj.insert(3)             
obj.insert(4)
obj.insert(5)
obj.display()
obj.middleElement()
obj.insert(6)
obj.display()
obj.middleElement()