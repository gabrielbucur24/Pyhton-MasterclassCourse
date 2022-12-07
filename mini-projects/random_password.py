import random

poss = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
while True:
    passlen = int(input("Enter how long the password you want to be: "))
    password = "".join(random.sample(poss, passlen))
    print(password)
