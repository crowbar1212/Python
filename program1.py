#!/bin/python3
print("Hello, World!")
name = input("What's your name? ")
print("Hello " + name, "on a scale of 1-10, how have you been coping with the Covid-19 pandemic? 1 being very poorly, 10 being very well")
while True:
    coping = input("Please enter a number, 1-10: ")
    try:
        val = int(coping)
        print("Thank you for your proper input.")
        if 1 <= val and val <= 3:
            infected = input("I'm so sorry to hear that. Were you or someone you know infected with Covid-19? Please say 1 for yes, 0 for no: ")
        elif 4 <= val and val <= 6:
            infected = input("I see, were you or someone you know infected with Covid-19? Please say 1 for yes, 0 for no: ")
        elif 7 <= val and val <= 10:
            infected = input("Good to hear you are doing well! Were you or someone you know infected with Covid-19? Please say 1 for yes, 0 for no: ")
        if infected:
            print("I'm so sorry")
        else:
            print("That's good to hear.")
        break
    except ValueError:
        try:
            val = float(coping)
            print("I'm sorry, the number should be a whole number,", val, "doesn't work")
        except ValueError:
            print("I'm sorry I'm looking for a number-digit, something like 1 or 4, two or six spelled out for example won't work")

