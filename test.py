class node(object):

	def __int__(self,data,next,prev):
		self.next = next
		self.prev = prev
		self.data = data

class linkedlist(object):

	head = None
	tail = None

	def insert(self,data):

		new_node = (data,None,None)

		if self.head is None:
			self.tail = self.head = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

	def remove(self, data):

		curnode = self.head

		while curnode not None:

			if curnode.data == data:

				if curnode.prev not None:

					curnode.prev.next = curnode.next
					curnode.next.prev = curnode.prev

				else:
					curnode.prev = None
					curnode.next = head.next
					
