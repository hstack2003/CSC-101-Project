# testing . . .
#test
#testing pull request

class Restaurant:
    def __init__(self, name:str, cuisine:str, price:int, rating:float):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __repr__(self):
        return ("Name: {}"
                "Cuisine: {}"
                "Price: {}"
                "Rating: {}"
                "Type: {}".format(self.name, self.cuisine,
                                  self.price, self.rating, self.m_type))
        #this is a test

cat_list = ["name", "cuisine", "price", "rating"]