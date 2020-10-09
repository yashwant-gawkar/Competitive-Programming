class node:
	def _init_ (self,data):
		self.data=data
		self.next=None

class L_L:
	def _init_ (self,head_val):
		self.head=node(head__val)
	def append(self,val):
		temp=head
		while temp.next:
			temp=temp.next
		temp.next=node(val)
	def print_l(self):
		temp=head
		while temp.next:
			print(temp.data)
			temp=temp.next

l=L_L(3)
l.append(4)
l.append(5)
l.print_l()
