from book_management import Book, BookManagement
from memeber_management import LibraryMember, MemberManagement
from error_handling import ErrorHandling, InvalidISBNError, NegativeQuantityError, NonExistentMemberError

class BorrowReturn:
    def __init__(self, book_management, member_management):
        self.book_management = book_management
        self.member_management = member_management

    def check_book_availability(self, title, quantity):
        if title in self.book_management.book_inventory:
            available_quantity = self.book_management.book_inventory[title].quantity
            return available_quantity >= quantity
        else:
            return False

    def update_book_quantity(self, title, quantity):
        if title in self.book_management.book_inventory:
            self.book_management.update_book(title, self.book_management.book_inventory[title].quantity - quantity)

    def borrow_book(self, member_id, title, quantity):
        try:
            ErrorHandling.validate_member_existence(member_id, self.member_management)
            ErrorHandling.validate_quantity(quantity)
            if self.check_book_availability(title, quantity):
                self.update_book_quantity(title, quantity)
                print(f"Member {member_id} borrowed {quantity} copies of '{title}'.")
            else:
                print(f"Book '{title}' not available in sufficient quantity.")
        except (InvalidISBNError, NegativeQuantityError, NonExistentMemberError) as e:
            print(f"Error: {e}")

    def return_book(self, member_id, title, quantity):
        try:
            ErrorHandling.validate_member_existence(member_id, self.member_management)
            ErrorHandling.validate_quantity(quantity)
            self.update_book_quantity(title, -quantity)
            print(f"Member {member_id} returned {quantity} copies of '{title}'.")
        except (InvalidISBNError, NegativeQuantityError, NonExistentMemberError) as e:
            print(f"Error: {e}")
