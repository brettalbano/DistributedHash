import FingerTable

class Node():

 	"""docstring for Node"""

 	def __init__(self, id_):
 		self.id_ = id_
 		self.fingerTable_ = None
 		self.localKeys_ = {}
 		self.successor = None

 	def join(self, node):
 		#TODO: implement node join function
 		#Arguments:
 		# node: type Node
 		#   the first node to contact with to initialize join process
 		#   If this is the first node to join the Chord network, the
 		#   parameter is None.
 		#Return value:
 		# void

 	def find(self, key):
 		#TODO: implement DHT lookup
 		#Taking the psuedo code from the Chord paper Figure 4
 		#Arguments:
 		# key: type unit8_t
 		#Return:
 		# value: type unit8_t

 		keys_successor = self.find_successor(key)
 		value = keys_successor.localKeys_[key]
 		return value

 	def insert(self, key):
 		#TODO: implement DHT key insertion
 		#Arguments:
 		# key: type unit8_t
 		#Return:
 		# void

 	def remove(self, key):
 		#TODO: implement DHT key deletion
 		#Arguments:
 		# key: type unit8_t
 		#Return:
 		# void

 	#################################################################
 	# Functions after this are helper functions to complete the tasks
 	# that are above
 	#################################################################

 	def find_successor(self, key):
 		#This method will return the node in which the network key
 		#id's data is located. This will be done by finding the
 		#  immediate predecessor node of the key and then return that
 		#  nodes successor
 		#Arguments:
 		# key: type unit8_t
 		#Return
 		# successor : type Node

		predecessor = self.find_predecessor(key)
		return predecessor.successor

	def find_predecessor(self, key):
		#This method will ask Node self to find id's predecessor by
		#  checking the intervals of the finger tables of this node
		#  and then find the closest precedeing finger
		#Arguments:
		# key: type unit8_t
		#Return:
		# predecessor : type Node

		predecessor = self

		# Check to see if key is not in the list created by range
		#  which is a range of this current Nodes id and it's
		#  successors.
		# If it is not, then go through finger table to find a range
		# that it is.
		while key not in range(predecessor.id_,
							   predecessor.successor.id_):
			predecessor = predecessor.closest_preceding_finger(key)

		return predecessor

	def closest_preceding_finger(self, key):
		#This method will find the finger that has the closest id
		# to the key but still less or equal to the value of key

		#This for loop is attempting to go from the last index
		# that the finger table contains and work backwords.
		# in C++ this would look closer to this:
		#  for(int i = m-1, i <=1, i--)
		# where m is the number of bits in the identifiers.
		# TODO: Change the range format to a more robust
		#       expression that will accept any value for m
		#   	in range(0, 7)
		for finger_num in range(len(self.fingerTable_)).reverse():
			if self.fingerTable_[finger_num]


