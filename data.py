

class Restaurant:
    def __init__(self, name:str, cuisine:str, price:int, rating:float, m_type:str):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating
        #type; potentially redundant?
        self.m_type = m_type

    def __repr__(self):
        return ("Name: {}"
                "Cuisine: {}"
                "Price: {}"
                "Rating: {}"
                "Type: {}".format(self.name, self.cuisine,
                                  self.price, self.rating, self.m_type))

