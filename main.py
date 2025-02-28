from data import Restaurant

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


#hello function made by Diego and Hannah
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


#category search function made by Hannah and Diego
def category_search(cats:list[int]) -> None:
    for num in cats:
        if num in cat_numbers:
            pref = input("What are you looking for in category {}?\n> ".format(cat_numbers[num]))
            user_prefs[cat_numbers[num]] = pref.lower().strip()

# compiles results function made by Hannah and Diego
def compile_results(prefs:dict[str, None]) -> dict[str, list[str]]:
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
        rating_res = [restaurant for restaurant in restaurants if str(restaurant.cuisine) == user_prefs["rating"]]
        user_res["rating"] = rating_res
    if len(user_res["name"]) == 0 and len(user_res["cuisine"]) == 0 and len(user_res["price"]) == 0 and len(user_res["rating"]) == 0:
        print("No search results are available for that search query.\n"
              "Do you want to search again?\n")

    return user_res




#main structure made by Hannah and Diego
def main():
    # says hello to user and brings up search options
    hello()

    # Category Select:
    # In a loop, asks the user for the categories that the user wants to search by.
    cats = category_select()

    # Category Search:
    category_search(cats)

    #Category compile
    results = compile_results(user_prefs)
    if results:


    #score restaurants and create one dict


if __name__ == "__main__":
    print(main())





