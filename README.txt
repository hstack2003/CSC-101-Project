PYELP: a program to help indecisive users decide where to eat

Description:
    Our program will ask users what restaurant categories or attributes they care about (i.e. name, cuisine, price, and rating).
    Then, within in their preferred categories, we will ask what specifically they are looking for, such as Indian or dessert for cuisine, or a three out of five for priciness.
    Next, we will go through our list of restaurants to match restaurant attributes to their preferences.
    We will then present the user with a text file of restaurants that match their preferences best.

Files:
    main.py (driver file): contains our main program, functions, and database of Restaurants
    data.py: contains Restaurant class definition and methods
Text files:
    pyelp.txt: contains the Restaurants that meet the user's preferences

Classes:
    class Restaurant:
    def __init__(self, name:str, cuisine:str, price:int, rating:float):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __repr__(self):
        return ("{}\n "
                "\tCuisine: {}\n "
                "\tPrice: {}/5 $\n "
                "\tRating: {} stars\n\n".format(self.name.title(), self.cuisine.title(),
                                  self.price, self.rating))

    def __eq__(self, other):
        return (self is other or type(self) == type(other) and self.name == other.name
                and self.cuisine == other.cuisine and self.price == other.price and self.rating == other.rating)

Lists:
    restaurants: contains all the objects of class Restaurant in our database
    cats: the integers corresponding to the categories the user is searching for
    results_list: list of Restaurants that meet at lease one of the user's preferences

Dictionaries:
    cat_numbers = {1:"name", 2:"cuisine", 3:"price", 4:"rating"}
        dictionary that links search categories to integers so user can easily search

    user_prefs = {"name":None, "cuisine":None, "price":None, "rating":None}:
        dictionary containing the user's specific preference for each category

    user_res = {"name":[], "cuisine":[], "price":[], "rating":[]}:
        dictionary whose values are lists of Restaurants that match user preferences in each category

    reps = {}
        dictionary that will contain restaurant names as keys and integers counting the number of preferences they match (ie the number of times they appear in the values of the user_res dictionary)



Prototypes of all functions with documentation. The documentation will include - purpose of the function, usage of all arguments to the functions, usage of return type of the function. An example is listed below for your reference:

# Function greets the user
# no inputs or output
def hello():

# category select function asks the user to type the integers corresponding to the categories for which they have preferences
# input is integers from user
# output is a list of integers (cats) corresponding to the categories for which they have preferences
def category_select() -> list[int]:

# category search function asks the user what their preference is for each selected category
# input is the cats list
# no output,but adds preferences to user_prefs dictionary
def category_search(cats:list[int]) -> None:

# compile results function finds Restaurants whose attributes match the preferences for each category in user_prefs
# input is user_prefs
# output is none if no matches or a dictionary user_res which contains a list of restaurants that match preferences as values for each category (keys)
def compile_results(prefs:dict[str, None]) -> Optional[dict[str, list[Restaurant]]]:

# trimmed_list function creates a list of all restaurants that match at least one preference
# input is the user_res list
# output is a list: results_list
def trimmed_list(results:dict[str, list[Restaurant]]) -> list[Restaurant]:

# repetitions function will figure out how many preferences each restaurant matches according to how many times it appears as a value in the user_res dictionary
# input is user_res dictionary
# output is reps dictionary which has restaurant names as keys and integer counts as values
def repetitions(results:dict[str, list[Restaurant]]) -> dict[str, int]:

# results_to_text function turns the results list into a text file
# input is results_list
# creates a text file
def results_to_text(final_list:list[Restaurant]) -> None:

# main structure contains all the functions our program needs to run
# no inputs or outputs
def main():
    hello()
    cats = category_select()
    category_search(cats)
    results = compile_results(user_prefs)
    if not results:
        print("We couldn't find anything based on your search terms.")
        choice = input("Would you like to try again? (Y or N) \n>").lower()
        if choice == "y":
            main()
        else:
            print("ok...i see how it is...\n")
            exit()
    final = trimmed_list(results)
    repetitions(results)
    results_to_text(final)
    return "Your results are stored in the Pyelp.txt file!"
