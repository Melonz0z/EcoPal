def shopping(): #shopping function - maia

    # give some advice about environmentally friendly shopping
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

    print("working on this")

    
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

        b = input("!shopping - sustainable places to shop \n !tips - everyday ways to be sustainable \n !vehicles - eco friendly vehicles and alternatives \n !volunteering - volunteering oppurtunities \n !donating - where to donate \n  ")

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
