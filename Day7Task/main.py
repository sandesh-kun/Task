from book_management import Book, BookManagement
from memeber_management import LibraryMember, MemberManagement
from borrow_return import BorrowReturn
from report_generation import ReportGeneration
from error_handling import InvalidISBNError, NegativeQuantityError, NonExistentMemberError

def main():
    book_management = BookManagement()
    member_management = MemberManagement()
    borrow_return_module = BorrowReturn(book_management, member_management)
    report_generation_module = ReportGeneration(book_management, member_management)

    while True:
        print("\nMain Menu:")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Borrowing and Returning")
        print("4. Report Generation")
        print("5. Exit")

        try:
            command = int(input("Enter your command: "))

            if command == 1:
                book_management_menu(book_management)
            elif command == 2:
                member_management_menu(member_management)
            elif command == 3:
                borrow_return_menu(borrow_return_module)
            elif command == 4:
                report_generation_menu(report_generation_module)
            elif command == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input.")

def book_management_menu(book_management):
    print("\nBook Management Menu:")
    print("1. Add Book")
    print("2. Update Book Quantity")
    print("3. Remove Book")

    try:
        book_command = int(input("Enter your command: "))

        if book_command == 1:
            add_book_menu(book_management)
        elif book_command == 2:
            update_book_quantity_menu(book_management)
        elif book_command == 3:
            remove_book_menu(book_management)
        else:
            print("Invalid")

    except ValueError:
        print("Invalid input.")

def add_book_menu(book_management):
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        date_published = input("Enter book publication date (YYYY-MM-DD): ")
        quantity = int(input("Enter book quantity: "))

        book = Book(title, author, date_published, quantity)
        book_management.add_book(book)
        print(f"Book '{title}' added successfully.")

    except ValueError:
        print("Invalid input for quantity. Please enter a valid number.")

def update_book_quantity_menu(book_management):
    title = input("Enter the title of the book: ")
    try:
        new_quantity = int(input("Enter the new quantity: "))
        book_management.update_book(title, new_quantity)
        print(f"Book quantity for '{title}' updated successfully.")
    except ValueError:
        print("Invalid input for quantity. Please enter a valid number.")

def remove_book_menu(book_management):
    title = input("Enter the title of the book to remove: ")
    book_management.remove_book(title)
    print(f"Book '{title}' removed successfully.")

def member_management_menu(member_management):
    print("\nMember Management Menu:")
    print("1. Add Member")
    print("2. Update Member Contact")
    print("3. Remove Member")

    try:
        member_command = int(input("Enter your command: "))

        if member_command == 1:
            add_member_menu(member_management)
        elif member_command == 2:
            update_member_contact_menu(member_management)
        elif member_command == 3:
            remove_member_menu(member_management)
        else:
            print("Invalid")

    except ValueError:
        print("Invalid input.")

def add_member_menu(member_management):
    try:
        member_id = int(input("Enter member ID: "))
        name = input("Enter member name: ")
        contact = input("Enter member contact: ")

        member = LibraryMember(member_id, name, contact)
        member_management.add_member(member)
        print(f"Member '{name}' added successfully.")

    except ValueError:
        print("Invalid input for member ID.")

def update_member_contact_menu(member_management):
    member_id = int(input("Enter the ID of the member: "))
    new_contact = input("Enter the new contact information: ")
    member_management.update_member(member_id, new_contact)
    print(f"Member contact for ID {member_id} updated successfully.")

def remove_member_menu(member_management):
    member_id = int(input("Enter the ID of the member to remove: "))
    member_management.remove_member(member_id)
    print(f"Member with ID {member_id} removed successfully.")

def borrow_return_menu(borrow_return_module):
    print("\nBorrowing and Returning Menu:")
    print("1. Borrow Book")
    print("2. Return Book")

    try:
        borrow_return_command = int(input("Enter your command: "))

        if borrow_return_command == 1:
            borrow_book_menu(borrow_return_module)
        elif borrow_return_command == 2:
            return_book_menu(borrow_return_module)
        else:
            print("Invalid.")

    except ValueError:
        print("Invalid input.")

def borrow_book_menu(borrow_return_module):
    member_id = int(input("Enter member ID: "))
    title = input("Enter the title of the book to borrow: ")
    try:
        quantity = int(input("Enter the quantity to borrow: "))
        borrow_return_module.borrow_book(member_id, title, quantity)
    except ValueError:
        print("Invalid input for quantity.")

def return_book_menu(borrow_return_module):
    member_id = int(input("Enter member ID: "))
    title = input("Enter the title of the book to return: ")
    try:
        quantity = int(input("Enter the quantity to return: "))
        borrow_return_module.return_book(member_id, title, quantity)
    except ValueError:
        print("Invalid input for quantity. Please enter a valid number.")

def report_generation_menu(report_generation_module):
    print("\nReport Generation Menu:")
    print("1. Generate Book Inventory Report")
    print("2. Generate Member Borrowing Report")

    try:
        report_command = int(input("Enter your command: "))

        if report_command == 1:
            generate_book_inventory_report_menu(report_generation_module)
        elif report_command == 2:
            generate_member_borrowing_report_menu(report_generation_module)
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def generate_book_inventory_report_menu(report_generation_module):
    sort_by = input("Enter sorting option (title/author/date_published/quantity): ")
    report_generation_module.generate_book_inventory_report(sort_by)

def generate_member_borrowing_report_menu(report_generation_module):
    report_generation_module.generate_member_borrowing_report()

if __name__ == "__main__":
    main()
