class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.books = {}

  def get_email(self):
    return self.email

  def change_email(self, address):
    self.email = address
    return print("E-mail address updated to " + str(self.email) + "\n")

  def __repr__(self):
    return print("Name: " + str(self.name) + "\n" + "E-mail: " + str(self.email)+ "\n" + "Books read: " + str(len(self.books)) + "\n")

  def __eq__(self, other_user):
    if self.name == other_user.name and self.email == other_user.email:
      return True
    else:
      return False
        
  def read_book(self, book_object, rating = None):
    if book_object not in self.books:
      self.books[book_object] = rating
    else:
      print("This book has already been read.\n")
  
  def get_average_rating(self):
    total_rating = 0
    for value in self.books.values:
      total_rating += value
    return total_rating / len(self.books.values)

class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []
  
  def get_title(self):
    return self.title
  
  def get_isbn(self):
    return self.isbn
  
  def set_isbn(self, new_isbn):
    self.isbn = new_isbn
    return print(str(self.title) + " ISBN updated to " + str(self.isbn) + "\n")
  
  def add_rating(self, rating = None):
    if type(rating) is int:
      if rating >= 0 and rating <= 4:
        self.ratings.append(rating)
    else:
      print("Invalid rating.\n")

  def __eq__(self, other_book):
    if self.title == other_book.title and self.isbn == other_book.isbn:
      return True
    else:
      return False
  
  def get_average_rating(self):
    total_rating = 0
    for i in self.ratings:
      total_rating += value
    return total_rating / len(self.ratings)
  
  def __hash__(self):
    return hash((self.title, self.isbn))

class Fiction(Book):
  def __init__(self, title, author, isbn):
    super().__init__(title, isbn)
    self.author = author
    
  def get_author(self):
    return self.author
  
  def __repr__(self):
    return "{title} by {author}\n".format(title = self.title, author = self.author)

class NonFiction(Book):
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level
    
  def get_subject(self):
    return self.subject
  
  def get_level(self):
    return self.level
  
  def __repr__(self):
    return "{title}, a {level} manual on {subject}\n".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater():
  def __init__(self):
    self.users = {}
    self.books = {}
    print("\n--- WELCOME TO TOMERATER ---\n")
    
  def create_book(self, title, isbn):
    new_book = Book(title, isbn)
    print("Created new book: {book}\n".format(book=title))
    return new_book
  
  def create_novel(self, title, author, isbn):
    new_novel = Fiction(title, author, isbn)
    print("Created new novel: {book}\n".format(book=title))
    return new_novel
  
  def create_non_fiction(self, title, subject, level, isbn):
    new_non_fiction = NonFiction(title, subject, level, isbn)
    print("Created new non-fiction book: {book}\n".format(book=title))
    return new_non_fiction
  
  def add_book_to_user(self, book_object, email, rating = None):
    key_to_check = email
    if email in self.users:
      name = self.users.get(email)
      name.read_book(book_object, rating)
      book_object.add_rating(rating)
      if book_object in self.books:
        self.books[book_object] += 1
        print("+1 to {book_object} in the TomeRater book list\n".format(book_object = book_object))
      else:
        self.books[book_object] = 1
        print("New entry for {book_object} in the TomeRater book list\n".format(book_object = book_object))
    else:
      print("No user with email {email}!".format(email = email))
    
  def add_user(self, name, email, books = []):
    if email not in self.users.keys():
      new_user = User(name, email)
      self.users[email] = new_user
      print("User: {name} added".format(name = name))
      if len(books) > 0:
        print(str(name) + " has already read " + str(len(books)) + " books.\n")
        for book in books:
          print(str(book) + " added to " + str(name) + ".\n")
          self.add_book_to_user(book, email)
      else:
        print("Books read: 0\n")
    else:
      print("This user already exists.\n")
  
  def print_catalog(self):
    print("Catalogue:")
    for key in self.books.keys():
      print(str(key))
  
  def print_users(self):
    print("Users:")
    for key in self.users.keys():
      print(str(key))
    print("\n")
  
  def most_read_book(self):
    most_read_book = ""
    count = 0
    print("Most read book:")
    for book, reads in self.books.items():
      if reads >= count:
        most_read_book == book
    return most_read_book

  def highest_rated_book(self):
    highest_rated_book = ""
    count = 0
    print("Highest rated book:")
    for key in self.books.keys():
      if key.get_average_rating() >= count:
        highest_rated_book == key
    return highest_rated_book

  def most_positive_user(self):
    most_positive_user = ""
    count = 0
    print("Most positive user:")
    for key in self.users.keys():
      if key.get_average_rating() >= count:
        most_positive_user == key
    return most_positive_user
    