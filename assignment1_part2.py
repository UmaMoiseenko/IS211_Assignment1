class Book(object):
	def __init__( self, author='', title='' ):
		self.author = author
		self.title = title

	def display(self):
		print  '%s, written by %s' % (self.title, self.author)


if __name__ == '__main__':
    book1 = Book('John Steinbeck', 'Of Mice and Men')
    book2 = Book('Harper Lee', 'To Kill a Mockingbird')
    book1.display()
    book2.display()