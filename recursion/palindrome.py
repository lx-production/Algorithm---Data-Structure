import string


def is_palindrome(phrase):
    # base case
    if len(phrase) < 2:
        return True

    text = phrase.lower()

    text = ''.join([letter for letter in text if letter in
                    (string.ascii_lowercase + string.digits)])

    # divide into easier calculation
    # and recursive operation
    return phrase[0] == phrase[-1] and is_palindrome(phrase[1:len(phrase) - 1])
