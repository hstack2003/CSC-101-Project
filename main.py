from data import Restaurant, cat_list

restaurants = [Restaurant("Firestone", "barbecue", 4, 5),
               Restaurant("Woodstock", "pizza", 4, 4.5),
               Restaurant("Scout Coffee", "cafe", 3, 4.5),
               Restaurant("Flour House", "italian", 5, 5),
               Restaurant("McConnell's", "dessert", 3, 4.5)]

user_data = []

def hello():
    print("hello")

def help_cats():
    print("Your category options are:")
    for cat in cat_list:
        print(cat)

def divider():
    print("----------------------- \n")

def main():
    # says hello to user and brings up search options
    hello()

    while True:
        category = input("What category do you want to search by?\n"
                         "(If you are done, enter 'done')\n"
                         "(If you need the list of categories, enter 'help')\n"
                         " > ")
        category = category.lower().strip()
        divider()
        if category in cat_list:
            user_data.append(category)
        elif category == "done" or len(user_data) == 4:
            break
        elif category == "help":
            help_cats()
        else:
            print("Not a valid category. Enter something else!")
            divider()

    print("you survived!")



if __name__ == "__main__":
    main()



    #Options to sort by name or other attributes
    #If statements to discern between commands.
    #Random function
    #Add your own?



