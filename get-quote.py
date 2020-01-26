import random

rnd = random.randint(0,13)
f = open("quotes.txt")
quotes = f.readlines()
f.close()
print(quotes[rnd])
