import os
import datetime
from book_management import BookManagement
from memeber_management import MemberManagement

class ReportGeneration:
    def __init__(self, book_management, member_management):
        self.book_management = book_management
        self.member_management = member_management

    def generate_timestamp(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d_%H-%M-%S")

    def create_report_directory(self):
        timestamp = self.generate_timestamp()
        directory_name = f"reports_{timestamp}"
        os.makedirs(directory_name)
        return directory_name

    def generate_book_inventory_report(self, sort_by='title'):
        sorted_books = sorted(self.book_management.book_inventory.values(), key=lambda x: getattr(x, sort_by))
        report_content = "\n".join(str(book) for book in sorted_books)

        report_directory = self.create_report_directory()
        report_filename = os.path.join(report_directory, f"book_inventory_report_{self.generate_timestamp()}.txt")

        with open(report_filename, 'w') as file:
            file.write(report_content)

        print(f"Book Inventory Report generated at: {report_filename}")

    def generate_member_borrowing_report(self):
        report_content = "\n".join(str(member) for member in self.member_management.library_members)

        report_directory = self.create_report_directory()
        report_filename = os.path.join(report_directory, f"member_borrowing_report_{self.generate_timestamp()}.txt")

        with open(report_filename, 'w') as file:
            file.write(report_content)

        print(f"Member Borrowing Report generated at: {report_filename}")