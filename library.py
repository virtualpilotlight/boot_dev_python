class Book:
  def __init__(self, title, author):
      self.title = title
      self.author = author
      self.available = True
  def checkout(self):
    if self.available == True:
      self.available = False
      return True
    else:
      return False
  def return_book(self):
    self.available = True
  def display_info(self):
    print(f"book title: {self.title} book author: {self.author}")
book1 = Book("Chobits", "CLAMP")
book2 = Book("Dangerous Angels", "Franchesca Lia Block")
book3 = Book("A Scanner Darkly", "PKD")
books = [book1, book2, book3]
for book in books:
  book.display_info()