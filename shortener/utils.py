import random
import string


def make_short_url(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
