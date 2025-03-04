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


