"""

**Personal comments:
Was hitting an issue of forgetting to set the address of my first node back to its original address. 
Everytime I returned the function it would point to the tail from my previous iteration, and I would only return a 2 element list everytime.
**
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""
 
def Insert(head, data):
    #print "we want to insert {} at the end".format(data)
    #print "head address is :"
    #print head
    start_node = head # save address of head.
    if head != None:#if a linked list, go to the last node.
        #Create new node with data.
        new_node = Node()
        new_node.data = data
        new_node.next = None
        #print new_node.next
        #print new_node
        while head.next != None:# find tail node
            #print "current head with value{}".format(head.data)
            #print head
            #print "current node data"
            #print head.data
            head = head.next
            #print "leaving while loop, this should be the last node"
            #print head
            #print head.data
            #print "next node data"
            #print head.data
        #print head.next
        #print "setting new tail"
        head.next = new_node #insert new node at the end.
        #print head.next
        #print head.next #this should be none
    else: #empty list, initialize the linked list.
        head = Node(data)
        head.next = None
        #print "list was empty, initializing a new list"
        start_node = head
        #print head #This should be the address for the entire function.  
    """
    print "showing entire list"
    if start_node != None:
        print_node = start_node
        while print_node.next != None:
            print print_node.data
            print_node = print_node.next
        print print_node.data
    """
    return start_node