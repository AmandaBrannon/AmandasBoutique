name = input("Hi! Welcome to Amanda's Boutique! Whats your name? ")
balance = int(325)
location = int(1)
occasion = int(6)
shirtcolor = int(1)
panttype = int(1)
dresscolor = int(1)
hatcolor = int(1)
jewelrytype = int(1)
print(name + "! Its nice to meet you! It looks like you have $325 to spend!")
print("So here at this boutique, we sell a variety of items,")
while int(balance) > int(0):
    location = input("What would you like to look at? shirts(1), pants(2), dresses(3), hats(4), or jewelry(5)? ")
    if int(location) == int(1):
        print("Oh shirts! nice choice!")
        shirtcolor = input("We have pink(1), polka-dot(2), blue(3), and black(4), and they are each $25! Back(5) ")
        if int(shirtcolor) == int(1):
            print("Nice! The pink shirt! Pink is my favorite color!")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(shirtcolor) == int(2):
            print("Nice! The polka-dot shirt! Spots are definitely in right now!")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(shirtcolor) == int(3):
            print("Nice! The blue shirt! Perfect for a family picnic!")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(shirtcolor) == int(4):
            print("Black is so classic and goes with everything!")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(shirtcolor) == int(5):
            print("Back")
        else:
            print ("We have some great options, I promise!")


    elif int(location) == int(2):
        print("Pants! super cool!")
        panttype = input("We have Jeans(1), slacks(2), work pants(3), and khackis(4), and they are each $50! Back(5) ")
        if int(panttype) == int(1):
            print("Jeans are perfect for any occasion!")
            balance -= int(50)
            print("your balance is now $" + str(balance))
        elif int(panttype) == int(2):
            print("A nice pair of slacks at a price you can't beat!")
            balance -= int(50)
            print("your balance is now $" + str(balance))
        elif int(panttype) == int(3):
            print("These bad boys can withstand any job, guaranteed!")
            balance -= int(50)
            print("your balance is now $" + str(balance))
        elif int(panttype) == int(4):
            print("A little bit of khaki never hurt nobody!")
            balance -= int(50)
            print("your balance is now $" + str(balance))
        elif int(panttype) == int(5):
            print("Back")
        else:
            print ("Someone likes to be adventurous. Well there's nothing here")


    elif int(location) == int(3):
        print("Amazing! I love dresses too!")
        dresscolor = input("We have paisleys(1), argyle(2), sparkly pink(3), and black(4), and they are each $75! Back(5) ")
        if int(dresscolor) == int(1):
            print("Paisleys are certainly making a comeback!")
            balance -= int(75)
            print("your balance is now $" + str(balance))
        elif int(dresscolor) == int(2):
            print("I love this pattern on you!")
            balance -= int(75)
            print("your balance is now $" + str(balance))
        elif int(dresscolor) == int(3):
            print("Everyone needs a little more sparkle in their lives!")
            balance -= int(75)
            print("your balance is now $" + str(balance))
        elif int(dresscolor) == int(4):
            print("Every girl needs a LBD!")
            balance -= int(75)
            print("your balance is now $" + str(balance))
        elif int(dresscolor) == int(5):
            print("Back")
        else:
            print ("Do you want a cute dress or not?")


    elif int(location) == int(4):
        print("A good hat can make or break an outfit!")
        hatcolor = input("We have sunhats(1), baseball caps(2), fedoras(3), and propeller hats(4), and they are each $25! Back(5) ")
        if int(hatcolor) == int(1):
            print("Sun protection is VITAL! Great choice! But don't forget the sunscreen!")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(hatcolor) == int(2):
            print("Sporty yet chic! A classic!")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(hatcolor) == int(3):
            print("Erm, don't go living in your mom's basement now!")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(hatcolor) == int(4):
            print("These certainly make you feel like a kid again! Or like a club penguin character")
            balance -= int(25)
            print("your balance is now $" + str(balance))
        elif int(hatcolor) == int(5):
            print("Back")
        else:
            print ("These hats are flying off the shelves! AAAAHHHHH!")


    elif int(location) == int(5):
        print("Jewelry! Any special occasion?")
        occasion = input("1:yes 2:no ")
        if int(occasion) == int(1):
            print("Awww! I'm so happy for you!")
        elif int(occasion) == int(2):
            print("Doesn't matter! Any time is a good time for new jewlery!")
        elif int(occasion) == int(4623):
            print("I love you so much John! <3")
        else:
            print("Fine, keep your secrets")
        print("Anyway, what are we thinking?")
        jewelrytype = input("Some bracelets?(1) A necklace?(2) A ring perhaps?(3) and they are each $150! Back(5) ")
        if int(jewelrytype) == int(1):
            print("Bracelets can spice up any outfit!")
            balance -= int(150)
            print("your balance is now $" + str(balance))
        elif int(jewelrytype) == int(2):
            print("Remember, necklaces need to complement the neckline of your top, or else it will look funky!")
            balance -= int(150)
            print("your balance is now $" + str(balance))
        elif int(jewelrytype) == int(3):
            print("Rings are so gorgeous!")
            balance -= int(150)
            print("your balance is now $" + str(balance))
        elif int(jewelrytype) == int(5):
            print("Back")
        else:
            print("I'm so confused right now.")

    else:
        print("Girl what are you talking about?")

print("Well, it looks like you've run out of money " + name + "! No worries if you overspent,")
print("think of it as a parting gift. I hope to see you soon!")