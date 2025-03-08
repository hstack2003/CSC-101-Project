from data import Restaurant
from typing import Optional
# do we want to take the function descriptions from README and put above the functions in this file?
#restaurant data created by Hannah and Diego
restaurants = [Restaurant("firestone", "barbecue", 4, 5),
               Restaurant("woodstock", "pizza", 4, 4.5),
               Restaurant("scout coffee", "cafe", 3, 4.5),
               Restaurant("flour house", "italian", 5, 5),
               Restaurant("mcconnell's", "dessert", 3, 4.5),
               Restaurant("olive garden", "italian", 3, 3),
               Restaurant("high street deli", "sandwiches", 3, 4),
               Restaurant("finney's", "new american", 4, 4),
               Restaurant("petra", "greek", 3, 4.5),
               Restaurant("nick the greek", "greek", 3, 3),
               Restaurant("shin's sushi", "sushi", 4, 4.5),
               Restaurant("lincoln deli", "sandwiches", 3, 4),
               Restaurant("sally loo's", "cafe", 4, 5),
               Restaurant("jewel of india", "indian", 3, 3),
               Restaurant("nite creamery", "dessert", 4, 5),
               Restaurant("taqueria san miguel", "mexican", 3, 4),
               Restaurant("taqueria santa cruz", "mexican", 3, 4.5),
               Restaurant("splash cafe", "seafood", 3, 4.5),
               Restaurant("cool cat cafe", "burgers", 4, 4.5),
               Restaurant("red robin", "burgers", 3, 4.5),
               Restaurant("the krusty krab", "burgers", 5, 5),
               Restaurant("the chum bucket", "???", 1, 0),
               Restaurant("cj's", "barbecue", 3, 4)]
                #add more restaurants here

# Data storage created by Hannah and Diego
#cat_numbers: connects a key category number to its corresponding category
#cat_numbers = {1:"name", 2:"cuisine", 3:"price", 4:"rating"}

#user_prefs: connects a key category string to a specified user input
#user_prefs = {"name":None, "cuisine":None, "price":None, "rating":None}

#user_res: connects a key category to the list of restaurants that match satisfy the query for the given category.
#user_res = {"name":[], "cuisine":[], "price":[], "rating":[]}

#trimmed_res: a list of all restaurants, without repeats, that matched a user input
#trimmed_res = []

#reps: connects a restaurant name string to the amount of times it was repeated throughout the user_res dict
#reps = {}

#matches:connects a number (representing the amount of times repeated) to a restaurant name string.
#matches = {1:[], 2:[], 3:[], 4:[]}


# category select function asks the user to type the integers corresponding to the categories for which they have preferences
# input is integers from user
# output is a list of integers (cats) corresponding to the categories for which they have preferences
# category select function made by Diego and Hannah
def category_select() -> list[int]:
    cats = input("Enter numbers of the categories you wish to search by (with spaces!)\n"
                 "1 - Name\n"
                 "2 - Cuisine\n"
                 "3 - Price\n"
                 "4 - Rating\n"
                 "> ")
    cats = cats.split()
    return [int(num) for num in cats if num.isdigit() and 1 <= int(num) <= 4]


# category search function asks the user what their preference is for each selected category
# input is the cats list
# no output,but adds preferences to user_prefs dictionary
#category search function made by Hannah and Diego
def category_search(cats:list[int]) -> dict[str, Optional[str]]:
    cat_numbers = {1: "name", 2: "cuisine", 3: "price", 4: "rating"}
    prefs = {"name":None, "cuisine":None, "price":None, "rating":None}
    for num in cats:
        pref = input("What are you looking for in category {}?\n> ".format(cat_numbers[num]))
        prefs[cat_numbers[num]] = pref.lower().strip()
    return prefs


# compile results function finds Restaurants whose attributes match the preferences for each category in user_prefs
# input is user_prefs
# output is none if no matches or a dictionary user_res which contains a list of restaurants that match preferences as values for each category (keys)
# compiles results function made by Hannah and Diego
def compile_results(prefs:dict[str, None], data:[list[Restaurant]]) -> dict[str, list[Restaurant]]:
    res = {"name": [], "cuisine":[], "price":[], "rating":[]}
    if prefs["name"]:
        name_res = [restaurant for restaurant in data if restaurant.name == prefs["name"]]
        res["name"] = name_res
    if prefs["cuisine"]:
        cuisine_res = [restaurant for restaurant in data if restaurant.cuisine == prefs["cuisine"]]
        res["cuisine"] = cuisine_res
    if prefs["price"]:
        price_res = [restaurant for restaurant in data if str(restaurant.price) == prefs["price"]]
        res["price"] = price_res
    if prefs["rating"]:
        rating_res = [restaurant for restaurant in data if str(restaurant.rating) == prefs["rating"]]
        res["rating"] = rating_res
    return res



# trim_and_find_reps function creates a single list of resulting restaurants and identifies repetitions for later sorting
# input is the user_res list
# No output for this function. This function only alters outside lists
# trimmed_list function made by Hannah and Diego
def trim_and_find_reps(results:dict[str, list[Restaurant]]) -> tuple[list[Restaurant], dict[str, int]]:
    trimmed = []
    name_reps = {}
    for cat in results:
        for restaurant in results[cat]:
            if restaurant not in trimmed:
                trimmed.append(restaurant)
                name_reps[restaurant.name] = 1
            else:
                name_reps[restaurant.name] += 1
    return trimmed, name_reps


def results_sorting(results_list: list[Restaurant], reps:dict[str, int]) -> dict[int, list[Restaurant]]:
    matches = {1:[], 2:[], 3:[], 4:[]}
    for restaurant in results_list:
        if reps[restaurant.name] == 1:
            matches[1].append(restaurant)
        elif reps[restaurant.name] == 2:
            matches[2].append(restaurant)
        elif reps[restaurant.name] == 3:
            matches[3].append(restaurant)
        else:
            matches[4].append(restaurant)
    return matches

# results_to_text function turns the results list into a text file
# input is results_list
# creates a text file
#results_to_text function made by Hannah and Diego
def results_to_text(lst1:list[Restaurant], lst2:list[Restaurant], lst3:list[Restaurant], lst4:list[Restaurant], file_name:str) -> None:
    all_lists = [lst4, lst3, lst2, lst1]
    non_empties = [lst for lst in all_lists if lst]
    responses = ["Here are the best options!\n\n", "These are some great options too.\n\n", "These options are also worth looking at.\n\n", "Still looking? Try these!\n\n"]
    with open(file_name, 'w') as file:
        resp_idx = 0
        file.write("Here are our suggestions for you!\n\n")
        for lst in non_empties:
            file.write(responses[resp_idx])
            list_number = 1
            for rest in lst:
                file.write("{}.) {}".format(list_number, str(rest)))
                list_number += 1
            resp_idx += 1


#main structure made by Hannah and Diego
def main():
    print("Hello, welcome to Pyelp!\n"
          "We can help you find a restaurant to eat at.\n")
    cats = category_select()
    user_prefs = category_search(cats)
    user_res = compile_results(user_prefs, restaurants)
    if len(user_res["name"]) == 0 and len(user_res["cuisine"]) == 0 and len(user_res["price"]) == 0 and len(user_res["rating"]) == 0:
        print("We couldn't find anything based on your search terms.")
        choice = input("Would you like to try again? (Y or N) \n>").lower()
        if choice == "y":
            main()
        else:
            print("ok...i see how it is...\n")
            exit()
    trimmed_res, reps = trim_and_find_reps(user_res)
    matches = results_sorting(trimmed_res, reps)
    results_to_text(matches[1], matches[2], matches[3], matches[4], "pyelp.txt")
    return "Your results are stored in the Pyelp.txt file!"


if __name__ == "__main__":
    print(main())





