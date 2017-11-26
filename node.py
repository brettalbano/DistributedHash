class Node():

 	"""docstring for Node"""
 	
 	def __init__(self, id_):
 		self.id_ = id_
 		self.fingerTable_ = None
 		self.localKeys_ = {}

 	def join(node):
 		#TODO: implement node join function
 		#Arguments:
 		# node: type Node
 		#   the first node to contact with to initialize join process
 		#   If this is the first node to join the Chord network, the
 		#   parameter is None.
 		#Return value:
 		# void

 	def find(key):
 		#TODO: implement DHT lookup
 		#Arguments:
 		# key: type unit8_t
 		#Return:
 		# value: type unit8_t

 	def insert(key):
 		#TODO: implement DHT key insertion
 		#Arguments:
 		# key: type unit8_t
 		#Return:
 		# void

 	def remove(key):
 		#TODO: implement DHT key deletion
 		#Arguments:
 		# key: type unit8_t
 		#Return:
 		# void


