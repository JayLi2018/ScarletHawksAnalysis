"""
create a min-heap for storing player pairs
"""
import pandas as pd

class MinHeap:

	def __init__(self,data_list=[],key=None):

		self.data_list = data_list
		self.key = key

	def size(self):

		return len(self.data_list)


	def get_left_child_index(self,parent_index):

		return parent_index * 2 + 1

	
	def get_right_child_index(self,parent_index):

		return parent_index * 2 + 2


	def get_parent_index(self,child_index):

		return (child_index-1)//2   # // -- floor operator


	def hasLeftChild(self,index):

		return bool(self.get_left_child_index(index) <= self.size()-1)


	def hasRightChild(self,index):

		return bool(self.get_right_child_index(index) <= self.size()-1)


	def hasParent(self,index):

		return bool(self.get_parent_index(index)>=0)


	def getLeftChild(self,index):

		return self.data_list[self.get_left_child_index(index)]


	def getRightChild(self,index):

		return self.data_list[self.get_right_child_index(index)]


	def getParent(self,index):

		if(self.get_parent_index(index)>=0):
			return self.data_list[self.get_parent_index(index)]

	def swap(self,index_1, index_2):

		self.data_list[index_1], self.data_list[index_2] = self.data_list[index_2],self.data_list[index_1]


	def peek(self):

		if(self.size() == 0):
			raise Exception("There is no data to peek !")

		else:
			return(self.data_list[0])

	def heapifyUp(self):

		index = self.size()-1

		while(self.hasParent(index) and (self.getParent(index)[self.key].loc[0])>(self.data_list[index][self.key].loc[0])):

			self.swap(self.get_parent_index(index),index)
			index = self.get_parent_index(index)

	def heapifyDown(self):

		index = 0
		while(self.hasLeftChild(index)):
			smallerChildIndex = self.get_left_child_index(index)
			if(self.hasRightChild(index) and (self.getRightChild(index)[self.key].loc[0]) < (self.getLeftChild(index)[self.key].loc[0])):
				smallerChildIndex = self.get_right_child_index(index)
			if(self.data_list[index][self.key].loc[0]>self.data_list[smallerChildIndex][self.key].loc[0]):
				self.swap(index,smallerChildIndex)
			else:
				break
			index = smallerChildIndex


	def pop(self):

		if(self.size() == 0):
			raise Exception("There is no data to peek !")

		else:
			min_value = self.data_list[0]
			self.data_list[0] = self.data_list[-1]
			del self.data_list[-1]
			self.heapifyDown()

	def add(self,newdata):

		self.data_list.append(newdata)

		self.heapifyUp()

	def get_result(self):
		if(len(self.data_list)==0):
			return None
		else:
			return pd.concat(self.data_list)


# if __name__ == "__main__":

# 	heap = MinHeap(key='pm')

# 	list1 = [{"names":['a,b'],'pm':10},{"names":['c,b'],'pm':20},{"names":['a,c'],'pm':0},{"names":['a,e'],'pm':3},{"names":['e,f'],'pm':-12}]

# 	for n in list1:
# 		heap.add(n)
# 		print(heap.data_list)
# 		print("heap size is " + str(heap.size()))
# 		print("has parent? " + str(heap.hasParent(heap.size()-1)))

# 		print("\n")

# 	print(heap.peek())

# 	heap.pop()
# 	print(heap.data_list)

