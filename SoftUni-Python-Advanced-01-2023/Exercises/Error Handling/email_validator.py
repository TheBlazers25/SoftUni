class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """"Domain must be one of the following: .com, .bg, .org, .net"""
    pass

while True:
    email = input()

    if email == 'End':
        break

    try:
        if email.count('@') > 1:
            raise MustContainAtSymbolError

        if len(email.split('@')[0]) <= 4:
            raise NameTooShortError

        if '@' not in email:
            raise MustContainAtSymbolError

        if '.com' or '.bg' or '.org' or '.net' not in email:
            raise InvalidDomainError

        print('Email is valid')

    except IndexError:
        print('Invalid')

    email = input()

