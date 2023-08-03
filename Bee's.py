class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed {book.title}.")
                return
        print("Book not found or already borrowed.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned {book.title}.")
                return
        print("Book not found or already returned.")


    while True:
        print("\nWelcome To Blessed's Library Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.display_books()
        elif choice == 2:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print(f"{title} added to the library.")
        elif choice == 3:
            title = input("Enter book title to remove: ")
            for book in library.books:
                if book.title == title:
                    library.remove_book(book)
                    print(f"{title} removed from the library.")
                    break
            else:
                print("Book not found in the library.")
        elif choice == 4:
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == 5:
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == 6:
            print("Exiting Blessed's Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")