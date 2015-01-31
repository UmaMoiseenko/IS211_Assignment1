class ListDivideException(Exception):
	 """ Exception """
	pass

def listDivide( number, divide =2 ):
	result = 0

	try:
		for num in number: 
			if num%divide == 0:
				result+=1

	except:
		 raise MyException()

	print result
	return result

def testListDivide():
	try:
		listDivide([1,2,3,4,5])
		listDivide([2,4,6,8,10])
		listDivide([30, 54, 63,98, 100], divide=10)
		listDivide([])
		listDivide([1,2,3,4,5], 2) 

	except TypeError:
		raise ListDivideException

if __name__ == '__main__':
    testListDivide()
