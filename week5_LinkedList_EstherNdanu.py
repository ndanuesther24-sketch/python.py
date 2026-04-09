#Node class
class Node:
     def__init__(self,data):
        self.data = data
        self. next =None

# linked list classs
class LinkedList:
    def__init__(self):
        self .head = None

        def is_empty(self)
        return self .head is None

        def append(self,data):
            new_node =Node(data)
            if self. hand is None
            self . head =new_node
            return

            temp = self . head
            while temp . next :
                temp = temp . next
             temp . next = new_node

        def prepend(self,data) :
            new_node = Node(data)
            new_node . next =self.head
            self.head = new_node
        def insert_at_position(self,data,pos):
            if pos < 0 :
                print("invalid position")
                return

            temp = self .head 
            for _ in range(pos -1):
                if temp is None:
                    print("Position out of range")
                    return
                temp = temp .next

                if temp is None:
                    print("Position out of range")
                    return

                new_node = Node(data)
                new_node . next = temp.next
                temp . next = new_node
        
        def delete_by_value(self, value):
            temp = self .head

            if temp and temp .data == value:
                self .temp = temp.next
                return

            prev .next = temp.next
        def search(self,value):
            temp = self. head
            index = 0

            while temp:
                 if temp .dara == value:
                    return index
                temp = temp . next
                index+= 1

            return - 1

        def display(self):
            if self . head is None:
                print(List is empty)
                return

            temp = self . head
            while temp:
                print(temp .data, end="->")  
                temp = temp . next
             print(None)     

        def size(self):
            count = 0
            temp = self. head

            while temp:
                count += 1
                temp = temp. next

            return 

#Test section
if __name__ =="__main__":
    11 = LinkedList()
    print("Is list empty?" , 11. is_empty))

    11.append(10)
    11.append(20)
    11.append(30)

    11.prepend(5)

    11.insert_at_position(15,2)

    print("List after intersection:")
    11.display()

    print("Size:", 11.size()
    
    print("Search 20:, 11.search(20)")
    print("Search 100:, 11.search(100)")

    11.delete_by_value(10)
    print("List after deleting 10:")
    11.display()

    11.delete_by_value(100)

    print("Final Size",11.size())
    print("Is list emoty?", 11.is_empty())
    