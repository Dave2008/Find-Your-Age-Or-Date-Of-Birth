import time

print("Hey, Wanna find your age or date of birth?")
time.sleep(1.5)
print("You are at the right place")
time.sleep(1)
name = input("First, What's your name? ")
print("Hey " +name+ ". \n Please wait..." )
time.sleep(2)

app = input("Press 1 to find age or 2 to find date of birth: ")
if app == '1':
  print("loading...")
  time.sleep(2)
  atp = int(input("Year of Birth: "))
  print("Please wait...")
  time.sleep(2.5)
  ans = 2021 - atp
  print(f"{name},you are {ans} years old.")

elif app == '2':
  print("loading...")
  time.sleep(2)
  asp = int(input("Your Age: "))
  print("Please wait...")
  time.sleep(2.5)
  anw = 2021 - asp
  print(f"{name}, you were born in {anw}.")

else:
  print("Incorrect pin")
  
print("Hang on...")
time.sleep(3)  

won = input("If I'm right say  YES. If I am wromg say NO: ")  
if won == "YES":
  print("Thank you so much🤗. I'm glad it works")

elif won == "NO":
  print("Thank you. I will check if there is something wrong with the code")

else:
  print("Invalid answer")


