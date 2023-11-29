class InvalidISBNError(Exception):
    pass

class NegativeQuantityError(Exception):
    pass

class NonExistentMemberError(Exception):
    pass

class ErrorHandling:
    @staticmethod
    def validate_isbn(isbn):
        if not isinstance(isbn, str) or len(isbn) != 13 or not isbn.isdigit():
            raise InvalidISBNError("Invalid ISBN format. ISBN must be a 13-digit numeric string.")

    @staticmethod
    def validate_quantity(quantity):
        if quantity < 0:
            raise NegativeQuantityError("Quantity cannot be negative.")

    @staticmethod
    def validate_member_existence(member_id, member_management):
        if not any(member.member_id == member_id for member in member_management.library_members):
            raise NonExistentMemberError(f"Member with ID {member_id} does not exist.")
