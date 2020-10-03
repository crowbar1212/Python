#!/bin/python3
print("Hello, World!")
name = input("What's your name? ")
print("Hello " + name, "on a scale of 1-10, how have you been coping with the Covid-19 pandemic? 1 being very poorly, 10 being very well")
while True:
    coping = input("Please enter a number, 1-10: ")
    try:
        val = int(coping)
        print("Thank you for your proper input.")
        break
    except ValueError:
        try:
            float(coping)
            print("I'm sorry, the number should be a whole number,", val, "doesn't work")
            break
        except ValueError:
            print("I'm sorry I'm looking for a number-digit, something like 1 or 4, two or six spelled out for example won't work")

