#Binary search tree: Simplest implementation
#Dallas Johnson
#Data Structures CS-222

#Tree class: this is the top-level binary tree. This will only really store the root as a variable, and will house the search and modify methods.

class tree:
    root = None

    def __init__(self, rootNode = 0): #assuming that we arent' going to put in a node, but we totally can.
        root = rootNode

    def add(self, newNode): #Allows us to add a node to the tree, we may not be allowed to do this in program 4, but since a tree should know how to add nodes fuck it, we'll include this.
        if not root:
            root = newNode
        else:
            root.addNode(newNode)

#Node class: this is what holds our data. The class consists of the left node, right node, parent node, and the data. We'll also set a boolean flag for whether or not we're root.  

class node:
    parent = data = left = right = None #That initialization chain tho.
    count = 0 #If the two strings we're comparing are equal then we just add to this counter here.
    isRoot = False

    def __init__(self, newParent = None, newData = None, newLeft = None, newRight = None):
        parent = newParent
        data = newData
        left = newLeft
        right = newRight

        #We'll disable the root flag by default. I'm only doing this because it's never going to be root unless there's no parent set. If there's no parent then it must be part of it's own tree if another Root already exists.
        if not parent:
            isRoot = True

    def getRight(self): #returns the node to the left. We probably don't need to do this but I'm including these anyway.
        return right
    
    def setRight(self, newRight): #Allows us to declare a new right node.
        right = newRight

    def getLeft(self): #returns the node to the right. Again, probably overkill because python but I'm including them to be easily translated into c++ when the time comes.
        return left

    def setLeft(self, newLeft): #Allows us to set a new left node.
        left = newLeft

    def setData(self, newData): #Allows us to set data.
        data = newData

    def getData(self): #Allows us to return data from a node.
        return data

    #This is a relatively simple method. It's basically a recursive adding method that does one thing: adds a node. It's more boolean
    #because it's checking the string size. Smaller than goes left, greater than goes right.
    #If it's equal it'll increment the counter variable that each object will have when
    #instantiated.
    def addNode(self, newNode): #Recursive function for adding a node to the tree
        if newNode.getData() == data:
            count = count + 1
            return
        if newNode.getData() < data:
            if not left:
                left = newNode
            else:
                left.addNode(newNode)
        elif newNode.getData() > data:
            if not right:
                right = newNode
            else:
                right.addNode(newNode)

    #Deletion Rules made into their own methods for ease of use when deleting.

    def noChildRule(self):
        del self

    def singleChildRule(self):
        if not right:
            #This conditional checks which side that we're working on.
            #I may include a flag you can include later on, but this
            #is a pretty safe way to figure it out imo.
            #Left pointer on the parent
            if parent.getData() > data:
                temp = self
                parent.setLeft(left)
                del temp
            #Right pointer on the parent
            elif parent.getData() < data:
                temp = self
                parent.setRight(self)
                del temp
        elif not left:
            #Left pointer on the parent
            if parent.getData() > data:
                temp = self
                parent.setLeft(right)
                del temp
            #Right pointer on the parent
            elif parent.getData() < data:
                temp = self
                parent.setRight(right)
                del temp

    def doubleChildRule(self):
        currentNode = self
        finalLeft = None

        #Go right once. This is the first step in this method.
        finalLeft = right
        #We need to iterate the rest of the way down. A loop will suffice for this for simplicity's sake.
        while finalLeft.getLeft():
            finalLeft = finalLeft.getLeft()
        currentNode.setData(finalNode.getData())
        #Now we need to check and see which cases we have here. We shouldn't have any double children again, so now it's either
        #Single or no child rule.
        if not left and not right:
            noChildRule()
        elif not left or not right:
            singleChildRule()
                
                

    def delNode(self, newNode): #recursive remove function. There's three rules to this though
        #Rule one: if it's got no children we just delete it's shit.
        if not left and not right:
            noChildRule()
            return
        #Rule two: one child case: We move the pointer around then delete the node, we need the parent for this.
        elif not left or not right:
            #Handling the left pointer
            #I'm goign to include a conditional to know which pointer to work with on the parent.
            #If for some reason this gives an issue we're going to have to do something about it
            #later on.
            singleChildRule()
        else:
            #This is the two child case: If we have two children we need to go left once, right all the way down.
            #once we do that we copy the data from the far left node into the current one and delete the left node.
            #We'll do this by keeping track of the node we're deleting from. Then we'll store the final node in another variable and swap.
            #Then we'll delete that last node at the bottom.
            doubleChildRule()
