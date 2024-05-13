class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []

    def log_book_added(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("Book added to library:", args[1].title)
            return result
        return wrapper

    @log_book_added
    def add_book(self, book):
        self.books.append(book)

    def search_book(self, **kwargs):
        results = []
        for book in self.books:
            if all(getattr(book, key) == value for key, value in kwargs.items()):
                results.append(book)
        return results

    def display_books(self):
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("Genre:", book.genre)
            print()

 
    def iterate_books(self):
        for book in self.books:
            yield book

    def apply_to_books(self, func):
        results = []
        for book in self.books:
            results.append(func(book))
        return results

def display_book_info(book):
    return f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}"

def extract_title(book):
    return book.title

def check_genre(book):
    return book.genre == "Fiction"

def format_book_info(book):
    return f"{book.title} by {book.author} ({book.genre})"


my_library = Library()

# Add some books
my_library.add_book(Book("Harry Potter", "J.K. Rowling", "Fantasy"))
my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"))
my_library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"))

search_results = my_library.search_book(author="J.K. Rowling")
print("Search results:")
for book in search_results:
    print(display_book_info(book))

print("\nAll books in the library:")
my_library.display_books()

# Iterate over books using generator
print("\nIterating over books:")
for book in my_library.iterate_books():
    print(extract_title(book))

# Apply a function to each book
print("\nApplying function to each book:")
formatted_books = my_library.apply_to_books(format_book_info)
for book_info in formatted_books:
    print(book_info)
