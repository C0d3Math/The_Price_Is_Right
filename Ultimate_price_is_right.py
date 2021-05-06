#by @C0d3Math
#Made Thursday 5/6/2021

import random
import numpy as np

otherprize = random.choice(["car entertainment system", "turntable", "phone", "computer", "speaker", "security package"])
print("You won a " + str(otherprize) + "! Come on up here!")

game = random.choice([1,2,3])

if game == 1:
    #find the prices of the pairs
    pair1 = random.randrange(50,1000)
    pair1 = pair1/100
    pairs1and2 = False
    while pairs1and2 == False:
        pair2 = random.randrange(50,1000)
        pair2 = pair2/100
    if pair1 != pair2:
        pairs1and2 = True
    pair3matchey = False
    while pair3matchey == False:
        pair3 = random.randrange(50,1000)
        pair3 = pair3/100
    if pair1 != pair3 and pair2 != pair3:
        pair3matchey = True
    print("You can win a " + str(room) + " set in Pick A Pair!")
    print("Someone went to the grocery store and found 3 pairs of items. The items in each pair have the same price, but no two items in different pairs have the same price.")

    #set up most of the variables
    prices = [pair1, pair1, pair2, pair2, pair3, pair3]
    random.shuffle(prices)
    item = 100
    item2 = 100

    #pick an item and say the price of it
    while item not in [1,2,3,4,5,6]:
        print("Which item do you want? Item 1, 2, 3, 4, 5, or 6?")
        item = int(input())
        if item not in [1,2,3,4,5,6]:
            print("I didn't understand that. Please try again!")
    if prices[item - 1] == pair1:
        print("The price of the item is $"+ str(pair1) +".")
    elif prices[item - 1] == pair2:
        print("The price of the item is $"+ str(pair2) +".")
    else:
        print("The price of the item is $"+ str(pair3) +".")

    #choose the other item
    item2lalala = False
    while item2lalala == False:
        print("Choose another item. You can't choose the one you already chose.")
        item2 = int(input())
        if item2 not in [1,2,3,4,5,6]:
            print("I didn't understand that. Please try again!")
        elif item2 == item:
            print("You can't choose the same item. Please try again!")
        else:
            item2lalala = True
            
    #whether you win or not
    if prices[item - 1] == prices[item2 - 1]:
        print("You win!!")
    else:
        print("Sorry, you don't win.")
        if prices[item2 - 1] == pair1:
            print("The price of the other item is $"+ str(pair1) +".")
        elif prices[item2 - 1] == pair2:
            print("The price of the other item is $"+ str(pair2) +".")
        else:
            print("The price of the other item is $"+ str(pair3) +".")
        #second chance
        item3 = item2
        a = False
        while a == False:
            print("Which item do you want to keep? Type 1 or 2.")
            keeper = int(input())
            if keeper == 1:
                item2 = 0
                a = True
            elif keeper == 2:
                item = item2
                item2 = 0
                a = True
            else:
                print("I didn't understand that. Try again!")
        if prices[item - 1] == pair1:
            print("The price of the item that you kept is $"+ str(pair1) +".")
        elif prices[item - 1] == pair2:
            print("The price of the item that you kept is $"+ str(pair2) +".")
        else:
            print("The price of the item that you kept is $"+ str(pair3) +".")
        while item2 not in [1,2,3,4,5,6] or item2 == item or item2 == item3:
            print("What is your final item?")
            item2 = int(input())
            if item2 not in [1,2,3,4,5,6]:
                print("I didn't understand that. Try again!")
            elif item2 == item or item2 == item3:
                print("You can't choose any that you've already chosen. Choose another one!")
            else:
                print("Ok.")
        if prices[item - 1] == prices[item2 - 1]:
            print("You win!!")
        else:
            print("Sorry, you don't win. It's ok. At least you won a " + str(otherprize) + "!")
elif game == 2:
    SoSoPunchy = [1,10,100,1000,10000,100000,1000000,10000000,100000000]

    # print your winnings
    print("You can win as much as $" + str(SoSoPunchy[int(len(SoSoPunchy)) - 1]) + ", but as low as $" + str(SoSoPunchy[0]) + ".")

    # Set up most of the variables
    Ooferiz = [5,7,8,9,10,10,5,2,1]
    OhHi = 0
    keep = 'n'
    Holes = []
    NumberOfPunches = 4

    #Set up and print the number of punches
    for i in range(0, len(Ooferiz)):
        OhHi = OhHi + Ooferiz[i]    
    print("You have a choice of " + str(OhHi) + " punches.")

    #Set up the list of holes,print it, and then shuffle it
    for i in range(0, len(Ooferiz)):
        for j in range(1, Ooferiz[i] + 1):
            Holes.append(SoSoPunchy[i])
    print("The punches are: " + str(Holes) + ". But: They aren't in those positions.")
    random.shuffle(Holes)

    #The punching
    while NumberOfPunches != 0:
        if NumberOfPunches != 1:
            print("You have " + str(NumberOfPunches) + " punches remaining.")
        else:
            print("You have 1 punch remaining. Try to make it pretty good!")
        print("What is your guess? (1 to " + str(len(Holes)) + ")")
        Punch = input()
        Prize = Holes[int(Punch) - 1]
        if Prize != 0:
            print("You won $" + str(Prize) + "!!")
        else:
            print("You didn't win money. Good luck next time!") 
        if Prize == SoSoPunchy[int(len(SoSoPunchy)) - 1]:
            print("Wow! You won the grand prize!")
        NumberOfPunches = NumberOfPunches - 1
        if NumberOfPunches != 0:
            print("Do you want to punch again? (y/n)")
            keep = input()
            if keep == 'y':
                print("Punch again!")
            else:
                NumberOfPunches = 0
    if Prize != 0:
        print("Wow! You won money! Great job!")
    else:
        print("Oops.")
else:
    #set up all the digits of the price of the car, use them to calculate the price of the car, and roll the dice
    cartypes = ("Mazda CX-30","Ford F-150","Tesla Model 3","Tesla Model Y","Tesla Model X","Tesla Model S")
    car = random.choice(cartypes)
    CarDigit1 = random.randrange(1,7)
    CarDigit2 = random.randrange(1,7)
    CarDigit3 = random.randrange(1,7)
    CarDigit4 = random.randrange(1,7)
    CarDigit5 = random.randrange(1,7)
    DiceRoll1 = random.randrange(1,7)
    DiceRoll2 = random.randrange(1,7)
    DiceRoll3 = random.randrange(1,7)
    DiceRoll4 = random.randrange(1,7)
    carprice = str(CarDigit1)+str(CarDigit2)+","+str(CarDigit3)+str(CarDigit4)+str(CarDigit5)

    #beginning info
    print("You can win a " + car + "!")
    print("All numbers in the price of the car are 1 to 6.")
    print("The first number is " + str(CarDigit1) + ".")

    #roll the first die and find out whether you're right
    print("Your first dice roll is: " + str(DiceRoll1) + ".")
    if DiceRoll1 == CarDigit2:
        print("You rolled the second digit in the price of the car!")
        rightDigit2 = "y"
    else:
        print("Do you think the second digit is higher or lower than what you rolled? Input 'Hi' or 'Lo'.")
        bigDigit2=input()
        if bigDigit2 != "Hi" and bigDigit2 != "Lo":
            print("Sorry, I didn't understand that.")
            rightDigit2 = "n"
        elif bigDigit2 == "Hi" and CarDigit2 > DiceRoll1:
            rightDigit2 = "y"
        elif bigDigit2 == "Lo" and CarDigit2 < DiceRoll1:
            rightDigit2 = "y"
        elif bigDigit2 == "Hi" and CarDigit2 < DiceRoll1:
            rightDigit2 = "n"
        else:
            rightDigit2="n"

    #roll the second die and find out whether you're right
    print("Your second dice roll is: " + str(DiceRoll2) + ".")
    if DiceRoll2 == CarDigit3:
        print("You rolled the third digit in the price of the car!")
        rightDigit3 = "y"
    else:
        print("Do you think the third digit is higher or lower than what you rolled? Input 'Hi' or 'Lo'.")
        bigDigit3=input()
        if bigDigit3 != "Hi" and bigDigit3 != "Lo":
            print("Sorry, I didn't understand that.")
            rightDigit3 = "n"
        elif bigDigit3 == "Hi" and CarDigit3 > DiceRoll2:
            rightDigit3 = "y"
        elif bigDigit3 == "Lo" and CarDigit3 < DiceRoll2:
            rightDigit3 = "y"
        elif bigDigit3 == "Hi" and CarDigit3 < DiceRoll2:
            rightDigit3 = "n"
        else:
            rightDigit3="n"

    #roll the third die and find out whether you're right
    print("Your third dice roll is: " + str(DiceRoll3) + ".")
    if DiceRoll3 == CarDigit4:
        print("You rolled the fourth digit in the price of the car!")
        rightDigit4 = "y"
    else:
        print("Do you think the fourth digit is higher or lower than what you rolled? Input 'Hi' or 'Lo'.")
        bigDigit4=input()
        if bigDigit4 != "Hi" and bigDigit4 != "Lo":
            print("Sorry, I didn't understand that.")
            rightDigit4 = "n"
        elif bigDigit4 == "Hi" and CarDigit4 > DiceRoll3:
            rightDigit4 = "y"
        elif bigDigit4 == "Lo" and CarDigit4 < DiceRoll3:
            rightDigit4 = "y"
        elif bigDigit4 == "Hi" and CarDigit4 < DiceRoll3:
            rightDigit4 = "n"
        else:
            rightDigit4="n"

    #roll the fourth die and find out whether you're right
    print("Your fourth and final dice roll is: " + str(DiceRoll4) + ".")
    if DiceRoll4 == CarDigit5:
        print("You rolled the last digit in the price of the car!")
        rightDigit2 = "y"
    else:
        print("Do you think the last digit is higher or lower than what you rolled? Input 'Hi' or 'Lo'.")
        bigDigit5=input()
        if bigDigit5 != "Hi" and bigDigit5 != "Lo":
            print("Sorry, I didn't understand that.")
            rightDigit5 = "n"
        elif bigDigit5 == "Hi" and CarDigit5 > DiceRoll4:
            rightDigit5 = "y"
        elif bigDigit5 == "Lo" and CarDigit5 < DiceRoll4:
            rightDigit5 = "y"
        elif bigDigit5 == "Hi" and CarDigit5 < DiceRoll4:
            rightDigit5 = "n"
        else:
            rightDigit5="n"

    # whether you win and comments
    if rightDigit2 == "y" and rightDigit3 == "y" and rightDigit4 == "y" and rightDigit5 == "y":
        print("You won a $" + str(carprice) + " car!")
    else:
        print("Sorry, you did not win. The price of the car is $" + str(carprice) + ".")
    #What you got wrong
    if rightDigit2 == "n":
        print("You guessed wrong with your first dice roll. Sorry!")
    if rightDigit3 == "n":
        print("You guessed wrong with your second dice roll. Sorry!")
    if rightDigit4 == "n":
        print("You guessed wrong with your third dice roll. Sorry!")
    if rightDigit5 == "n":
        print("You guessed wrong with your fourth dice roll. Sorry!")
#info
print("It's time for you to spin the wheel!")

#first spin
spin1 = random.randrange(1,21)
spin1 = spin1 * 5
print("You spun a " + str(spin1) + "!")
if spin1 == 100:
    print("You spun a dollar!")
    #bonus spin
    print("You get a bonus spin. You won $1000. If you land on 5 or 15, the $1000 becomes $11000, but if you land it on the dollar, the $1000 becomes $26000!")
    bonus = random.randrange(1,21)
    bonus = bonus * 5
    if bonus == 5 or bonus == 15:
        print("You won $10000 in addition to your $1000!")
    elif bonus == 100:
        print("$25000! WOW!")
    else:
        print("None extra, sorry.")
else:
    a = False
    while a == False:
        print("Do you want to spin again? yes or no")
        spin = input()
        if spin in ["yes","y","Yes","Y"]:
            a = True
            #second spin
            spin2 = random.randrange(1,21)
            spin2 = spin2 * 5
            print("You spun a " + str(spin2) + "!")
            yourtotal = spin1 + spin2
            if spin1 + spin2 > 100:
                print("You busted.")
                bust = True
            elif spin1 + spin2 < 100:
                print("Your total is " + str(spin1 + spin2) + ".")
                bust = False
            else:
                bust = False
                print("You spun a dollar on the wheel!")
                 #bonus spin
                print("You get a bonus spin. You won $1000. If you land on 5 or 15, the $1000 becomes $11000, but if you land it on the dollar, the $1000 becomes $26000!")
                bonus = random.randrange(1,21)
                bonus = bonus * 5
                if bonus == 5 or bonus == 15:
                    print("You won $10000 in addition to your $1000!")
                elif bonus == 100:
                    print("$25000! WOW!")
                else:
                    print("None extra, sorry.")
        elif spin in ["no","n","No","N"]:
            a = True
            print("Your total is " + str(spin1) + ".")
        else:
            print("I didn't understand that. Please try again!")

#the other people's spins
spin1other1 = random.randrange(1,21)
spin1other1 = spin1other1 * 5
if spin1other1 < 60:
    spin2other1 = random.randrange(1,21)
    spin2other1 = spin2other1 * 5
    other1total = spin1other1 + spin2other1
else:
    other1total = spin1other1
spin1other2 = random.randrange(1,21)
spin1other2 = spin1other2 * 5
if spin1other2 < 60:
    spin2other2 = random.randrange(1,21)
    spin2other2 = spin2other2 * 5
    other2total = spin1other2 + spin2other2
else:
    other2total = spin1other2

#if they busted
if other1total > 100:
    print("Mark busted.")
    bust1 = True
else:
    bust1 = False
if other2total > 100:
    print("John busted.")
    bust2 = True
else:
    bust2 = False

#who s going to the showcase
if bust1 == True and bust2 == True:
    if bust == True:
        print("A triple bust! You, then, are going to the showcase!")
    else:
        print("You are going to the showcase!")
elif bust1 == True or bust2 == True:
    if bust == True:
        print("You are not going to the showcase.")
    else:
        if bust1 == True:
            if other2total > yourtotal:
                print("You are going to the showcase!")
            elif other2total == yourtotal:
                print("You tied, so are going to the showcase!")
            else:
                print("You are not going to the showcase.")
        else:
            if other2total > yourtotal:
                print("You are going to the showcase!")
            elif other2total == yourtotal:
                print("You tied, so are going to the showcase!")
            else:
                print("You are not going to the showcase.")
else:
    if yourtotal >= other1total and yourtotal >= other2total:
        print("You are going to the showcase!")
    else:
        print("You are not going to the showcase.")