age = input("Enter your age: ")
age = int(age)
have_own_car = input("Do you own your car (y/n):")

if(age >= 21):
  if have_own_car == 'y':
    print("You are over 21 years old and own your own car")
  else:
    print("You are over 21 years old and you DO NOT own your own car")
else:
  if have_own_car == 'y':
    print("You are younger than 21 years old and own your own car")
  else:
    print("You are younger than 21 years old you DO NOT own your own car")
