from random import*

coin={"heads":"heads","tails":"tails"}

bet=input("Make a bet. Heads or Tails? ")

if bet is not ["heads"] or ["tails"]:
    print("Spelling error? Go back to the editor and press F5!")
    exit()

else:
    for coin in range(1):
        coin=randint(0,1)

        if coin==0:
            print("The coin has been tossed!")
            print("You got Heads!")

        else:
            print("The coin has been tossed!")
            print("You got Tails!")

        
        
    
