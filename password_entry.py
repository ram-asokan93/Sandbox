"""
Ramkumar Asokan
"""
MIN_LENGTH = 4
MAX_LENGTH = 9

print("Enter a password: ")
print("\t Needs to be between {} and {} characters long".format(MIN_LENGTH, MAX_LENGTH))
password = input(">")

while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
    print("Enter a valid password: Between {} and {} characters".format(MIN_LENGTH, MAX_LENGTH))
    password = input("\t>")


print('Password accepted:')
print('*'*(len(password)))
