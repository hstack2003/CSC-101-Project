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

# trim_and_find_reps function creates a list of all restaurants that match at least one preference
# also creates a dictionary that has restaurant names as keys and integer counts as values (represent number of times the restaurant appears in user_res list, ie how many preferences it matches)
# input is the user_res list
# no return but adds to trrimmed_res list and dictionary reps
def trim_and_find_reps(results:dict[str, list[Restaurant]]) -> None:

# results_sorting function places all restaurants from an inputted list within a dictionary location depending on the number of times the restaurant was repeated in the search results according to the reps dict
# input is a list of restaurant objects. Will always be the trimmed_res list
# No output for this function. It will instead alter the global matches dictionary.

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
