import Node

class FingerTable():
    """docstring for FingerTable""" 
    
    def __init__(self, nodeId_):
        #Members:
        # node_Id : type uint8_t
        #   the id of node hosting the finger table
        # fingerTable_ : type Node[]
        #   this implementation will be different from Chord paper
        #   due to the inability to start a list from index 1.
        #   So this everywhere that is needing to access this list
        #   will show a -1 compared to Chord paper.
        self.nodeId_ = nodeId_ 
        self.fingerTable_ = []

    def set(self, index, successor):
        #Arguments:
        #  index : type size_t
        #  successor : type Node
        #Return:
        #  void
        self.fingerTable_[index] = successor

    def get(self, index):
        #Arguments:
        #  index : type size_t
        #     number of the finger table
        #Return:
        #   type : Node
        return self.fingerTable_[index]

    def prettyPrint(self):
        # TODO: complete the print function
        #This method will print the finger table in a nicely
        # formatted way to console.  
        