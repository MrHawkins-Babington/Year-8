print('What is the name of your app business?')
businessName = input()
print('The name of your business is',businessName)

print('What is your surname?')
surname = input()
print('Your surname is',surname)

print("What is your first name?")
firstname = input()
print("Hello",firstname,surname)

print("Your initials are:", firstname[0],surname[0])

fullname = firstname + " " + surname
print(fullname)

print(surname.upper())
print(firstname.upper())

print(len(firstname))
print(len(surname))

userS=surname[0:3]
userI=firstname[0]
userL=str(len(surname))
username2 = userS+userI+userL
print(username2)





