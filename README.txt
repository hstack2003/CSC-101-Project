PYELP: a program to help indecisive users decide where to eat

Description:
    Our program will ask users what restaurant categories or attributes they care about (i.e. name, cuisine, price, and rating).
    Then, within in their preferred categories, we will ask what specifically they are looking for, such as Indian or dessert for cuisine, or a three out of five for priciness.
    Next, we will go through our list of restaurants to match restaurant attributes to their preferences.
    We will then present the user with a text file of restaurants that match their preferences best.

Classes:
    Restaurant:
        Holds 4 attributes: The name of the restaurant, the type of food served (cuisine),
        the price of the restaurant (measured from 1-5, lowest being 1),
        and the rating of the restaurant (from 1-5 representing stars).
        The class also contains the __repr__ and __eq__ dunder functions to display the data and test equality.

Lists and Dictionaries:
    Defined and documented in the main.py file

Files:
    main.py (driver file): contains our main program, functions, and database of Restaurants
    data.py: contains Restaurant class definition and methods

Text files:
    pyelp.txt: contains the Restaurants that meet the user's preferences

Prototypes of all functions with documentation. The documentation will include - purpose of the function, usage of all arguments to the functions, usage of return type of the function. An example is listed below for your reference:

# category select function asks the user to type the integers corresponding to the categories for which they have preferences
# input is integers from user
# output is a list of integers (cats) corresponding to the categories for which they have preferences
def category_select() -> list[int]:

# category search function asks the user what their preference is for each selected category
# input is the cat_numbers list
# output is a dictionary of category strings and optional response strings
def category_search(cats:list[int]) -> None:

# compile results function finds Restaurants whose attributes match the preferences for each category in user_prefs
# input is user_prefs dictionary
# output is a dictionary user_res which contains a list of restaurants that match preferences as values for each category (keys)
def compile_results(prefs:dict[str, None]) -> Optional[dict[str, list[Restaurant]]]:

# trim_and_find_reps function creates a list of all restaurants that match at least one preference
# also creates a dictionary that has restaurant names as keys and integer counts as values (represent number of times the restaurant appears in user_res list, ie how many preferences it matches)
# input is the user_res list
# output is a tuple containing the results list of restaurant objects
def trim_and_find_reps(results:dict[str, list[Restaurant]]) -> None:

# results_sorting function places all restaurants from an inputted list within a dictionary location depending on the number of times the restaurant was repeated in the search results according to the reps dict
# input is a list of restaurant objects. Will always be the trimmed_res list
# output is a dictionary of integers and lists of restaurant objects
def results_sorting(results_list:list[Restaurant]) -> None:

# results_to_text function turns the results list into a text file
# input is results_list
# creates or overwrites the "pyelp.txt" text file
def results_to_text(final_list:list[Restaurant]) -> None:

# main structure contains all the functions our program needs to run
# no inputs or outputs
def main():
    print("Hello, welcome to Pyelp!\n"
          "We can help you find a restaurant to eat at.\n")
    cats = category_select()
    user_prefs = category_search(cats)
    user_res = compile_results(user_prefs, restaurants)
    if len(user_res["name"] == 0 and len(user_res["cuisine"] == 0 and len(user_res["price"] == 0 and len(user_res["rating"] == 0:
        print("We couldn't find anything based on your search terms.")
        choice = input("Would you like to try again? (Y or N) \n>").lower()
        if choice == "y":
            main()
        else:
            print("ok...i see how it is...\n")
            exit()
    trimmed_res, reps = trim_and_find_reps(user_res)
    matches = results_sorting(trimmed_res, reps)
    results_to_text(matches[1], matches[2], matches[3], matches[4])
    return "Your results are stored in the Pyelp.txt file!"
