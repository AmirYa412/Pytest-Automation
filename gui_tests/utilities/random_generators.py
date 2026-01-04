from random import randint
import string

def random_num(minimum, maximum):
    return randint(minimum, maximum)


def get_random_str(length: int):
    characters = string.ascii_letters + string.digits
    return ''.join([characters[randint(0, len(characters) - 1)] for i in range(length)])
