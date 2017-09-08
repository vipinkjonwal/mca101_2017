'''
Author				: Vipin Kumar
Course				: MCA101
Language			: Python
'''

def insertList(initialList,element,position=0):
	'''
	Objective		: To append a element in given sorted list.
	Input Variables	:
		initialList	: Sorted list inputted by user.
		element		: Element inputted by user needed to be appended.
		position	: default variable = 0  
	Return Value	: List, with the element appended at required position.
	'''
	#Approach		: Use recursion to check the position and then insert the element at given position.

	if element<initialList[len(initialList)-1]:
		if element<=initialList[position]:
			initialList.insert(position,element)
			return initialList
		else:
			return insertList(initialList,element,position+1)
	else:
		initialList.insert(len(initialList),element)
		return initialList

def main():
	'''
	Objective		: To append a element in given sorted list.
	Input Variables	: None.
	Return Value	: None.
	'''
	#Approach		: Invoke insertList function.
	initialList=[int(x) for x in input('Enter the list in sorted format: ').split()]
	element=int(input('Enter the element: '))
	print('List becomes: ',insertList(initialList,element))

if __name__ == '__main__':
	main()