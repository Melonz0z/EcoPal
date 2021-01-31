def shopping(): #shopping function - maia


     print("It is important to buy from places that value the environment.")


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
