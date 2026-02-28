import random
import hashlib
import time

def generate_Account_Number():
    return random.randint(10000000000,99999999999)

def generate_pin():
    return random.randint(1000,9999)

def encrypt_pin(s):
    return hashlib.sha384(str(s).encode()).hexdigest()

def outer_fun(func):
    def wrapper(*args,**kwargs):
        time.sleep(5)
        func(*args,**kwargs)
    return wrapper