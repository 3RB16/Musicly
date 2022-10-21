from .models import RoomModel
import string
import random


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        if RoomModel.objects.filter(code=code).count() == 0:
            break
    return code
