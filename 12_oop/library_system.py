from dataclasses import dataclass
# =====================================================================
# 1. DATA MODELS
# =====================================================================

@dataclass
class Book:
    isbn: str
    title: str
    author: str
    is_borrowed: bool = False

    def borrow(self) -> bool:
        if self.is_borrowed:
            print(f"Book '{self.title}' is already checked out.")
            return False
        else:
            self.is_borrowed = True
            print("Book borrowed successfully.")
            return True
    def return_book(self) -> bool:
        if self.is_borrowed:
            print("Book returned Successfully.")
            self.is_borrowed = False
            return True
        else:
            print("Book is not borrowed yet.")
            return False

class Member:
    borrow_limit = 5

    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book) -> bool:
        if len(self.borrowed_books) >= self.borrow_limit:
            print("You have reached your borrowing limit.")
            return False

        if book.borrow():
            self.borrowed_books.append(book)            
            return True
        else:
            print(f"'{book.title}' is currently not available.")
            return False

    def return_book(self, book: Book) -> bool:
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        else:
            print(f"Error: {self.name} did not borrow '{book.title}'.")
        return False

# =====================================================================
# 2. CORE LIBRARY SYSTEM (Controller)
# =====================================================================

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def register_member(self, member: Member) -> None:
        self.members.append(member)

    def search_books(self, query: str) -> list[Book]:
        clean_query = query.strip().lower()
        return [
            book for book in self.books
            if clean_query in book.title.lower() or clean_query in book.author.lower()]

    def display_all_books(self) -> None:
        if not self.books:
            print("There are no books in the library.")
            return
        for book in self.books:
            print(f"Title: {book.title} | " 
                  f"Status: {'Available' if not book.is_borrowed else 'Borrowed'} ")

    def find_book(self, isbn: str) -> Book | None:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id: int) -> Member | None:
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id: int, isbn: str) -> bool:
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member and book:
            return member.borrow_book(book)
        elif member is None:
            print(f"Error: Member with member ID {member_id} is not registered.")
            return False
        else:
            print(f"Error: Book with ISBN {isbn} is not found in catalog.")
            return False

    def return_book(self, member_id: int, isbn: str) -> bool:
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member and book:
            return member.return_book(book)
        elif member is None:
            print(f"Error: Member with member ID {member_id} is not registered.")
            return False
        else:
            print(f"Error: Book with ISBN {isbn} is not found in catalog.")
            return False
# =======================================================================
# 3. Standalone Functions
# =======================================================================
def get_safe_string(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        
        print("Invalid Input: Input cannot be blank.")

def get_safe_int(prompt:str) -> int:
    while True:
        try:
            user_input = int(input(prompt).strip())
            if user_input > 0:
                return user_input
            print("Please input a positive Number.")
        except ValueError:
            print("Input Error: Please input a valid Numerical value")


# =======================================================================
# 4. RUNTIME / USER INTERFACE
# =======================================================================

if __name__ == '__main__':
    library = Library()
    while True:
        print("=" * 45)
        print(f"{'LIBRARY MANAGEMENT SYSTEM':^45}")
        print("=" * 45)        
        print("1. Add Books")
        print("2. Register Members")
        print("3. Search Book by Title or Author")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Display All Books and their Status")
        print("7. Exit")
        print("=" * 45)
        try:
            user_choice = int(input("Please enter a choice (1-7): ").strip())
            if user_choice <= 0 or user_choice > 7:
                print("Invalid Choice: Please choose between 1 - 7.")
                continue
        except ValueError:
            print("Input Error: Please choose numerical value from 1 - 7.")
            continue

        if user_choice == 7:
            print("Thank you for using Library System. Goodbye!")
            break
        if user_choice == 1:
            print("\n--- ADD NEW BOOK ---")
            isbn = get_safe_string("Please enter ISBN of book: ")

            if library.find_book(isbn):
                print(f"Error: A book with ISBN {isbn} already exists in the catalog.")

            title = get_safe_string("Please enter the title of the book: ")
            author = get_safe_string("Please enter the Author of the book: ")
            
            book = Book(isbn, title, author)            
            library.add_book(book)
            print(f"Book '{title}' added Successfully.")

        elif user_choice == 2:
            print("\n--- REGISTER NEW MEMBER ---")
            member_id = get_safe_int("Please enter member ID: ")

            if library.find_member(member_id):
                print(f"Error: A member with ID {member_id} is already registered.")

            member_name = get_safe_string("Please enter your name: ")

            member = Member(member_id=member_id, name=member_name)
            library.register_member(member)
            print(f"Member '{member_name}' registered successfully.")

        elif user_choice == 3:
            print("\n--- SEARCH CATALOG ---")
            query = get_safe_string("Please Enter the title or author of the book: ")
            results = library.search_books(query)
            if results:
                print(f"\nFound {len(results)} matching book(s):")
                print("-" * 75)
                print(f"{'ISBN':<13} | {'Title':<25} | {'Author':<20} | {'Status'}")
                print("-" * 75)
                for book in results:
                    status = "Borrowed" if book.is_borrowed else "Available"
                    print(f"{book.isbn:<13} | {book.title:<25} | {book.author:<20} | {status}")
                print("=" * 75)
            else:
                print(f"No books found matching '{query}'.")

        elif user_choice == 4:
            print("\n--- BORROW BOOK TRANSACTION ---")
            member_id = get_safe_int("Please enter your member ID: ")
            isbn = get_safe_string("Please enter isbn of the book you want to borrow: ")
            success = library.borrow_book(member_id, isbn)
            if success:
                print("Transaction complete: Book successfully checked out.")

        elif user_choice == 5:
            print("\n--- RETURN BOOK TRANSACTION ---")
            member_id = get_safe_int("Please enter your member ID: ")
            isbn = get_safe_string("Please enter isbn of the book you want to return: ")

            success = library.return_book(member_id, isbn)
            if success:
                print("Transaction complete: Book successfully checked in.")

        elif user_choice == 6:
            print("\n--- COMPLETE CATALOG STATUS ---")
            library.display_all_books()

        input("\nPress Enter to return to the main menu...")