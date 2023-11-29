import datetime

class Book:
    def __init__(self, title, author, date_published, quantity):
        self.title = title
        self.author = author
        self.date_published = date_published
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.date_published}, Quantity: {self.quantity}"

class BookManagement:
    def __init__(self):
        self.book_inventory = {}

    def add_book(self, book):
        self.book_inventory[book.title] = book

    def update_book(self, title, new_quantity):
        if title in self.book_inventory:
            self.book_inventory[title].quantity = new_quantity

    def remove_book(self, title):
        if title in self.book_inventory:
            del self.book_inventory[title]
