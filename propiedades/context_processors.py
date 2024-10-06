import os
from django.utils.crypto import get_random_string

def get_unique_filename(instance, filename):
    extension = filename.split(".")[-1]
    unique_filename = f"{get_random_string(12)}.{extension}"
    return os.path.join("propiedades/", unique_filename)
