import random
#Write your code below this line 👇
print("Welcome to Coin Toss Program")
#Hint: Remember to import the random module first. 🎲
# Plan
# Generate random whole number between 1 and 0 and saved to a variable[done]
random_number = random.randint(0,1)
# check random number is working correctly[done]
# print(random_number);
# write a if/ else satement for if random number equals 0 then print Heads else print Tails
if random_number == 0:
  print("Heads")
else:
  print("Tails")
