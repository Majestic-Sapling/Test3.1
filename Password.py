import re

# this part of the code asks for the user's name
while True:
  name = input("Hello, what is your name?")
  if len(name) > 1 and name.isalpha():
    print ("Welcome, " + name)
    break
  elif name == "ESKETIT!":
    print ("Gucci Gang! For real though, please input a real name.")
  else:
    print ("Please input a real name")


print("")
print ("Hello, welcome to this password creator!")
print ("Your password must include one lowercase letter, one upperletter, one number, and one special character")
print("")

#this part of the code asks the user to create their password
while True:
  password = input("Please type in your password")
  if len(password) < 8:
    print ("Your password needs to have at least eight characters")
  elif not re.search('[a-z]', password):
    print ("Your password needs at least one lowercase character")
  elif not re.search('[A-Z]', password):
    print ("Your password needs at least one uppercase character")
  elif not re.search('[0-9]', password):
    print ("Your password needs at least one number")
  elif not re.search('[!@#$%^&*()_+=-]', password):
    print ("Your password needs at least one special character")
  else:
    print ("Your password is " + password)
