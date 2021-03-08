import random
#Setting variables
email = []
symbols = ["!", "#", "$", "%", "&"]
num_letters = int(input("Please choose the number of letters: "))
service = input("Please choose a sevice: ")
#1 Uppercase letter
for i in range(1):
    x = random.randint(66, 91)
    email.append(chr(x))
#1 Symbol
for i in range(1):
    x = random.choice(symbols)
    email.append(x)
#Letters
for i in range(num_letters - 3):
    x = random.randint(97, 122)
    email.append(chr(x))
#1 Number
for i in range(1):
    x = random.randint(1, 9)
    email.append(x)
#Print
semi_final = ''.join(map(str, email))
print(semi_final + "@" + service + ".com")