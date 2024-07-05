# Write a Python program that takes an integer input from the user and prints whether 
# the number is positive, negative or zero.

num = int(input("Enter a number: "))

if num<0:
  print("\n The number is NEGATIVE")
elif num == 0:
  print("\n The number is ZERO")
else:
  print("\n The number is POSITIVE")
          
