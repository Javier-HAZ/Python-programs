#working with linked lists a first approximation
# a linked list is a way of storing data in an ordered manner
#types single linked list: head->a->b->....->n->null
#double the direction is forward and backwards each node contains the address of the previous and next node
ar = [1,2,3,9]

class node:
    def __init__(self, data = None):
        self.data = data
        self.nextNode = None

class Linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.nextNode != None:
            current_node = current_node.nextNode
        current_node.nextNode = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.nextNode != None:
            total += 1
            cur = cur.nextNode
        return total
    
    def display(self):
        elems = []
        cur = self.head
        while cur.nextNode != None:
            cur = cur.nextNode
            elems.append(cur.data)
        print(elems)
    


  
    
my_list = Linked_list()
my_list.append(1)
my_list.append(3)
my_list.append(8)
my_list.display()

    



#simple exercise: 1-> 4-> 6-> 9-> 10
#creating the separate nodes

# node1 = node("1")
# node2 = node("4")
# node3 = node("6")
# node4 = node("9")
# node5 = node("10")

# #creating the conections

# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4
# node4.nextNode = node5

# current = node1

# while True:
#     print(current.data, " -> ", end="")
#     if current.nextNode is None:
#         print("None")
#         break
#     current = current.nextNode


        
        