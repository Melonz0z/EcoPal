import random

def shopping(): #shopping function - maia

    # give some advice about environmentally friendly shopping
    print ("Welcome to shopping tips!\n")

    print("It is important to buy from places that value the environment.")
    print ("When shopping, the best options to help the environment are to buy used. \nIf possible, try repairing"
    "an old item or borrowing from a friend if it's an item you do not plan to keep")
    print ("If you are buying something new, please think about if you realy need this item.")
    c = input("\nHow long do you plan on keeping this item?(one week or less, one month, forever)")
    
    if c == "one week or less":

        print ("\nPlease reconsider buying this item. It will not be worth it to you or the environment. Borrow it from a friend or rent if possible")
        print ("If you do have to buy it, please use it for as long as possible and be sure to discard/recycle accordingly")

    elif c == "one month":

        print ("\nThink about the environmental impact this products could potentially have. Please think about other buying options such as renting, borrowing from a friend, or buying used")
    
    elif c == "forever":

        print ("\nThis is excellent! Buying something you are planning to keep forever is ideal. Keep it up!")



def tips():

    print("Welcome to tips!\n")

    advice = ["Always dispose of items properly (either recycling, composting, or garbage", "Avoid fast fashion trends",
    "Limit your water use", "Buy used or repair items instead of buying new", "Look for energy efficient appliances", "Don't waste food",
    "Try to eat less meat"]

    tip = (random.choice(advice))
    print (tip)


    more = input("\nWould you like to learn more about this tip?(yes/no)")

    if more == "yes":
            i = advice.index(tip)
            if i == 0:
                print("You can check online with your local waste disposal facility to see what they reccomend. Make sure everything goes in the right bin.")               
            elif i == 1:
                print("Only buy things you truly want and need. Do not buy things because they are popular.")
            elif i == 2:
                print("There is a limited supply of clean, fresh water. Make sure you turn off taps you aren't using, take short showers and avoid unnecessary water use.")
            elif i == 3:
                print("There are so many people that throw things away just because they don't work. Looking into buying used" 
                " is often easy because of the number of products available. It is also often cheaper than buying new. Look on sites such as Kijiji and eBay")
            elif i == 4:
                print("Look for the most efficent applicance you can find!")
            elif i == 5:
                print("A lof of energy goes into food production around the world. Make sure you finish food that you buy")
            elif i == 6:
                print("Meat has a significant environmental impact due to what it takes to raise livestock(their food, land space and emissions). Try to limit meat consumption(especially red meat)"
                " to a reasonable amount for you. Anything helps!")
    else:
            print("Thanks for your time")

       


    
def vehicles():

    print("working on this")


def volunteering():

    print("working on this")


def donating():

    print("working on this")


def main():

    help = "!help"
    
    a = input("Hello! I'm EcoPal, your guide in living a more sustainable lifestyle. type !help for a list of commands \n")

    if a == "!help": 

        #list of commands for the user to say -maia

        b = input("!shopping - sustainable places and ways to shop \n !tips - everyday ways to be sustainable \n !vehicles - eco friendly vehicles and alternatives \n !volunteering - volunteering oppurtunities \n !donating - where to donate \n  ")

        # figure out what they selected from the menu
        if b == "!shopping":
            shopping()
        elif b == "!tips":
            tips()
        elif b == "!vehicles":
            vehicles()
        elif b == "!volunteering":
            volunteering()  
        elif b == "!donating":
            donating()
        else:
            print ("Please enter a valid response")  
    

    else:

        print("please type !help to get started!") #reminds user to type !help -maia

    

main()
