import random
last = 13
rnd = ramdon.randint(0, last)
  print(quotes[rnd])
def primary():
  print("Hello World")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13])

if __name__== "__main__":
  primary()
