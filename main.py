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
               Restaurant("nick the greek", "greek", 3, 3),
               Restaurant("nite creamery", "dessert", 4, 5),
               Restaurant("taqueria san miguel", "mexican", 3, 4),
               Restaurant("taqueria santa cruz", "mexican", 3, 4.5)]
                #add more restaurants here

# Data storage created by Hannah and Diego
cat_numbers = {1:"name", 2:"cuisine", 3:"price", 4:"rating"}
user_prefs = {"name":None, "cuisine":None, "price":None, "rating":None}
user_res = {"name":[], "cuisine":[], "price":[], "rating":[]}
reps = {}


# hello function made by Diego and Hannah
# hello(): Says hello to user to start program
# input: None
# output: None
def hello():
    print("Hello!\n"
          "Welcome to Pyelp!\n"
          "We can help you find a restaurant to eat at.\n")


#category select function made by Diego and Hannah
def category_select() -> list[int]:
    cats = input("Enter numbers of categories you wish to search by (with spaces!)\n"
                 "1 - Name\n"
                 "2 - Cuisine\n"
                 "3 - Price\n"
                 "4 - Rating\n"
                 "> ")
    cats = cats.split()
    return [int(num) for num in cats if num.isdigit() and 1 <= int(num) <= 4]

#do we want this to return user_prefs?
#category search function made by Hannah and Diego
def category_search(cats:list[int]) -> None:
    for num in cats:
        if num in cat_numbers:
            pref = input("What are you looking for in category {}?\n> ".format(cat_numbers[num]))
            user_prefs[cat_numbers[num]] = pref.lower().strip()


# compiles results function made by Hannah and Diego
def compile_results(prefs:dict[str, None]) -> Optional[dict[str, list[Restaurant]]]:
    if prefs["name"]:
        name_res = [restaurant for restaurant in restaurants if restaurant.name == user_prefs["name"]]
        user_res["name"] = name_res
    if prefs["cuisine"]:
        cuisine_res = [restaurant for restaurant in restaurants if restaurant.cuisine == user_prefs["cuisine"]]
        user_res["cuisine"] = cuisine_res
    if prefs["price"]:
        price_res = [restaurant for restaurant in restaurants if str(restaurant.price) == user_prefs["price"]]
        user_res["price"] = price_res
    if prefs["rating"]:
        rating_res = [restaurant for restaurant in restaurants if str(restaurant.rating) == user_prefs["rating"]]
        user_res["rating"] = rating_res
    if len(user_res["name"]) == 0 and len(user_res["cuisine"]) == 0 and len(user_res["price"]) == 0 and len(user_res["rating"]) == 0:
        return None
    return user_res

# trimmed_list function made by Hannah and Diego
def trimmed_list(results:dict[str, list[Restaurant]]) -> list[Restaurant]:
    results_list = []
    for cat in results:
        for restaurant in results[cat]:
            if restaurant not in results_list:
                results_list.append(restaurant)
    return results_list


# repetitions function made by Hannah and Diego
def repetitions(results:dict[str, list[Restaurant]]) -> dict[str, int]:
    for cat in results:
        for restaurant in results[cat]:
            if restaurant.name in reps:
                reps[restaurant.name] += 1
            else:
                reps[restaurant.name] = 1
    return reps


#results_to_text function made by Hannah and Diego
def results_to_text(final_list:list[Restaurant]) -> None:
    with open("pyelp.txt", 'w') as file:
        file.write("Here are our suggestions for you!\n\n")
        for rest in final_list:
            file.write(str(rest))

#main structure made by Hannah and Diego
def main():

    hello()

    # Category Select:
    # In a loop, asks the user for the categories that the user wants to search by.
    cats = category_select()

    # Category Search:
    category_search(cats)

    #Category compile
    results = compile_results(user_prefs)
    if not results:
        print("We couldn't find anything based on your search terms.")
        choice = input("Would you like to try again? (Y or N) \n>").lower()
        if choice == "y":
            main()
        else:
            print("ok...i see how it is...\n")
            exit()

    # score restaurants and create one dict
    final = trimmed_list(results)

    # identify how many times each restaurant is returned
    repetitions(results)

    #applies final results to text file
    results_to_text(final)

    return "Your results are stored in the Pyelp.txt file!"


if __name__ == "__main__":
    print(main())





