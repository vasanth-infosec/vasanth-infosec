import random
def passgen():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    numbers ="1234567890"
    symbols = "!@#$%^&*"
    all_chars = lower + upper + numbers + symbols
    length = int(input("Enter the length of Password : "))
    password = "".join(random.sample(all_chars,length))
    print("Grenerated Password : ",password)
    