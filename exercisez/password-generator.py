import random


# password generator
def password_generator(count_char=8):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'y', 'z']
    passw = []
    for i in range(count_char):
        passw.append(random.choice(arr))
    return "".join(passw)


newPass = password_generator(15)
print(newPass)
