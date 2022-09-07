#python 3.7.1

import random
import string

print("Hello world! \nThis is a random password generator.")

length = int(input("Desired password length: "))
char = string.ascii_letters + string.ascii_letters + string.ascii_letters + string.digits + string.digits + string.punctuation
task = "yes"
yes_responses, no_responses = {"y","yes", "Y", "Yes"}, {"n","no", "N", "No"}

while task in yes_responses:
    concat = random.sample(char,length)
    pwd = "".join(concat)
    print("Your new random password is:", pwd)
    task = None
    task = input("Do you want to generate another password? Input y/n:")

while task not in yes_responses and task not in no_responses:
    task = input("I can't understand that, try again with y/n:")
             
print("\nThanks for using this random password generator. \nHave a nice day!")
