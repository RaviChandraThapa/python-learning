from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    pages: int

class SmartBook:
    def __init__(self, title: str, price: float, copies: int):
        self.title = title
        self._price = 0
        self.price = price
        self.copies = copies

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Error: price must be greater than 0.")
            
        else:
            self._price = value

    @property
    def copies(self) -> int:
        return self._copies

    @copies.setter
    def copies(self, value: int) -> None:
        if value < 0:
            print("Error, Copies can not be negative.")
            self._copies = 0
        else:
            self._copies = value

if __name__ == "__main__":
    book = Book("Python Basics", "Ravi", 100)
    print(book)

    smart_book = SmartBook("Clean Code", 2500.0, 5)
    print(smart_book.price)
    print(smart_book.copies)

    smart_book.price = -100.0
    smart_book.copies = -10

    print(smart_book.price)
    print(smart_book.copies)