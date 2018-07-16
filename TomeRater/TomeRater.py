class User(object):
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User's email has been updated!")

    def read_book(self, book, rating = None): 
    	self.books.update({book: rating})

    def get_average_rating(self):
    	if len(self.books) > 0:
    		rating = 0
    		for value in self.books.values():
    			if not value == None:
    				rating += value
    		return rating/len(self.books)

    def __eq__(self, other_user):
        if self.name.lower() == other_user.name.lower() and self.email.lower() == other_user.email.lower():
        	return True
        else:
        	return False

    def __repr__(self):
        return "User {}, email: {}, books read: {}.".format(self.name, self.email, len(self.books))


class Book():
	def __init__(self, title, isbn):
		self.title = str(title)
		self.isbn = int(isbn)
		self.ratings = []

	def get_title(self):
		return self.title

	def get_isbn(self):
		return self.isbn

	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print("Book’s ISBN has been updated!")

	def add_rating(self, rating):
		if not rating == None:
			if rating >= 0 and rating <= 4:
				self.ratings.append(rating)
			else:
				print("Invalid Rating")

	def get_average_rating(self):
		if len(self.ratings) > 0:
			rating = 0
			for value in self.ratings:
				if not value == None:
					rating += value
			return rating/len(self.ratings)
		else:
			return 0
			
	def __hash__(self):
		return hash((self.title, self.isbn))

	def __eq__(self, other_book):
		if self.title.lower() == other_book.title.lower() and self.isbn == other_book.isbn:
			return True
		else:
			return False

	def __repr__(self):
		if len(self.ratings) > 0:		
			return "{}. ISBN: {}. Average user rating: {}".format(self.title, self.isbn, sum(self.ratings)/len(self.ratings))
		else:
			return "{}. ISBN: {}.".format(self.title, self.isbn)


class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author

	def get_author(self):
		return self.author

	def __repr__(self):
		return "{} by {}".format(self.title, self.author)


class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = str(subject)
		self.level = str(level)

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return "{}, a {} manual on {}".format(self.title, self.level, self.subject)


class TomeRater():
	def __init__(self):
		self.users = {}
		self.books = {}

	def create_book(self, title, isbn):
		for book in self.books.keys():
			if book.get_isbn() == isbn:
				print("This ISBN is already used!")
				return book
		else:
			new_book = Book(title, isbn)
			self.books.update({new_book: 0})
			return new_book

	def create_novel(self, title, author, isbn):
		for book in self.books.keys():
			if book.get_isbn() == isbn:
				print("This ISBN is already used!")
				return book
		else:
			new_book = Fiction(title, author, isbn)
			self.books.update({new_book: 0})
			return new_book

	def create_non_fiction(self, title, subject, level, isbn):
		for book in self.books.keys():
			if book.get_isbn() == isbn:
				print("This ISBN is already used!")
				return book
		else:
			new_book = Non_Fiction(title, subject, level, isbn)
			self.books.update({new_book: 0})
			return new_book

	def add_book_to_user(self, book, email, rating = None):
		if not email in self.users.keys():
			print("No user with email: {}!".format(email))
		else:
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			if not book in self.books.keys():
				self.books.update({book: 1})
			else:
				self.books[book] += 1

	def add_user(self, name, email, user_books = None):
		if "@" in email and email.endswith((".com", ".edu", ".org")):
			if email in self.users.keys():
				print("User already exists!")
			else:
				self.users[email] = User(name, email)
				if not user_books == None: 
					for book in user_books:
						self.add_book_to_user(book, email)
		else:
			print("Invaid e-mail address!")

	def print_catalog(self):
		print("Contents of the catalog:")
		for book in self.books.keys():
			print(book)

	def print_users(self):
		print("Users list:")
		for user in self.users.values():
			print(user)

	def most_read_book(self):
		most = 0
		for book, times_read in self.books.items():
			if times_read > most:
				most = times_read
				most_read_book = book
		return most_read_book

	def highest_rated_book(self):
		highest_rating = 0
		for book in self.books.keys():
			rating = book.get_average_rating()
			if rating > highest_rating:
				highest_rating = rating
				highest_rated = book
		return highest_rated

	def most_positive_user(self):
		highest_rating = 0
		for user in self.users.values():
			user_rating = user.get_average_rating()
			if user_rating > highest_rating:
				highest_rating = user_rating
				most_positive = user
		return most_positive

	def __eq__(self, other):
		for book in self.books.keys():
			if not book in other.books.keys():
				return False
		for user in self.users.keys():
			if not user in other.users.keys():
				return False
		return True


	def __repr__(self):
		all_contents = "Contents of the catalog:\n"
		for book in self.books.keys():
			all_contents += book.get_title()
			all_contents += "\n"
		all_contents += "\nActive users:\n"
		for user in self.users.keys():
			all_contents += user
			all_contents += "\n"

		return all_contents