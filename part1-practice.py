#......taking input and printing it......
#name = input("Type your name, then press enter: ")
#age = input("Type your age, then press enter: ")
#favcolor = input("Type your favorite color, then press enter: ")

#print(name)
#print(age)
#print(favcolor)

#....Build a program that asks the user to input their exam score and then prints a message
# score = int(input("Type your exam score and then press enter: "))
# if score > 90: 
#     print("Excellent!")
# elif score >= 70:
#     print("Good.")
# else: 
#     print("Needs improvement.")

#...make a sentence: 
# Convert it to uppercase.Remove any leading or trailing whitespace.
# Replace a word with another word of your choice.Split it into a list of words.

# sentence = "I'm just a lady with a lot of rabbits."
# print(sentence.upper())
# print(sentence.strip())
# print(sentence.replace("lot", "bunch"))
# print(sentence.split())

#create a name generator combining first and last names
#HAVING TROUBLE WITH THE RANDOM IMPORT, I THINK... GET HELP ON THIS ONE!!!!!!!!!!!!!
# import random
# first_names = ["bug", "berry", "bonita", "treasure", "atom"]
# last_names = ["porter", "blakey", "planes", "peters", "walston"]

# random_first = first_names.random.choice()
# random_last = last_names.random.choice()
# random_name = random_first + " " + random_last

# print(random_name)

#................discounted groceries bill........................
# milk = 5
# eggs = 3
# coffee = 10

# total_of_items = int(milk) + int(eggs) + int(coffee)
# discount = (10 / 100) * total_of_items
# discounted_total = total_of_items - discount

# print(total_of_items)
# print(discounted_total)

#...............simple calculator....................
# Ask the user to input two numbers.
# num1 = input("Type a number, then press enter: ")
# num2 = input("Type another number, then press enter: ")

# num1int = int(num1)
# num2int = int(num2)

# Perform basic arithmetic operations (add, subtract, multiply, divide) on the inputs.
# add = num1int + num2int
# subtract = num1int - num2int
# multiply = num1int * num2int
# divide = num1int / num2int

# # Display the results.
# print(add)
# print(subtract)
# print(multiply)
# print(divide)

#......Design a program that will help someone decide between two activities based on the weather and mood:
# Ask the user for the weather (sunny or raining) and their mood (happy or tired)
# weather = input("Type whether it is sunny or raining right now and then press enter: ")
# mood = input("Tell me if you're happy or tired right now and then press enter: ")

# # Based on the inputs, print one of the following suggestions: go for a hike, relax indoors
# if weather == "sunny" and mood == "happy":
#     print("Go for a hike!")
# elif weather == "sunny" and mood == "tired":
#     print("Stay in and relax.")
# else:
#     print("Stay in and rest.")

#............... Write a program where the user has to guess a secret number between 1 and 10. 
# The program should provide feedback if the guess is too high or too low 
# and congratulate the user if they guess correctly.

# Randomly select a secret number between 1-10.
#....PROBABLY NEED RANDOM IMPORT HERE <-------------COMPLETE AFTER RANDOM IMPORT SOLUTION*****
#import random
# num_list = list(range(1,11))
# secret_num = random.num_list()

# # Ask the user to make a guess between 1-10.
# guess = input("Guess a number 1-10 and the press enter: ")

# # If the user is correct, print "Congratulations, You guessed the secret number!"
# if int(guess) == secret_num:
#     print("You guessed it!")
# # If the user is too low, print "Too low!"
# elif int(guess) < secret_num:
#     print("Too low!")
# # If the user is too high, print "Too high!"
# else: 
#     print("Too high!")

