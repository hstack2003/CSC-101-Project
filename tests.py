import main
from data import Restaurant
from main import compile_results, trim_and_find_reps, results_sorting, results_to_text, restaurants
import unittest

class Testcases(unittest.TestCase):

    # Note that category_select() function is not testable due to taking user input
    # Here are example inputs that showcase how the function input and output works and avoids errors:
    # input: "1234 1" ---> output: [1]
    # input: "1 2 3 4" ---> output: [1, 2, 3, 4]

    # Note that category_search() function is not testable due to taking user input
    # Here are example inputs that showcase how the function input and output works and avoids errors:
    # input question: "What are you looking for in category cuisine?"
    # input: "burgers"
    # output appends user_prefs dictionary to {"name":None, "cuisine":"burgers, "price":None, "rating":None}


    def test_compile_results_1(self):
        user_prefs = {"name":None, "cuisine":"sushi", "price":None, "rating":None}
        expected = {"name":[], "cuisine":[Restaurant("shin's sushi", "sushi", 4, 4.5)],
                    "price":[], "rating":[]}
        results = compile_results(user_prefs, restaurants)
        self.assertEqual(expected, results)

    def test_compile_results_2(self):
        user_prefs = {"name": None, "cuisine": "pizza", "price": '5', "rating": None}
        expected = {"cuisine": [Restaurant("woodstock", "pizza", 4, 4.5)], "name": [],
                    "price": [Restaurant("flour house", "italian", 5, 5), Restaurant("the krusty krab", "burgers", 5, 5)], "rating": []}
        results = compile_results(user_prefs, restaurants)
        self.assertEqual(expected, results)


    def test_trim_and_find_reps_1(self):
        res = {"cuisine": [Restaurant("woodstock", "pizza", 4, 4.5)], "name": [],
                    "price": [Restaurant("flour house", "italian", 5, 5), Restaurant("the krusty krab", "burgers", 5, 5)], "rating": []}
        trimmed = []
        name_reps = {}
        result = main.trim_and_find_reps(res)
        expected = ([Restaurant("woodstock", "pizza", 4, 4.5), Restaurant("flour house", "italian", 5, 5), Restaurant("the krusty krab", "burgers", 5, 5)], {'flour house':1, 'the krusty krab':1, 'woodstock':1})
        self.assertEqual(result, expected)

    def test_trim_and_find_reps_2(self):
        res = {"cuisine": [Restaurant("flour house", "italian", 5, 5),
                           Restaurant("olive garden", "italian", 3,3)],
               "name":[],
               "price":[],
               "rating":[Restaurant("olive garden", "italian", 3, 3),
                         Restaurant("nick the greek", "greek", 3, 3),
                         Restaurant("jewel of india", "indian", 3, 3)]}

        trimmed = [Restaurant("flour house", "italian", 5,5),
                   Restaurant("olive garden", "italian", 3, 3),
                   Restaurant("nick the greek", "greek", 3, 3),
                   Restaurant("jewel of india", "indian", 3, 3)]

        name_reps = {"flour house": 1, "olive garden": 2, "nick the greek": 1, "jewel of india": 1}

        result = trim_and_find_reps(res)
        self.assertEqual((trimmed, name_reps), result)


    def test_results_sorting_1(self):
        matches = {1: [], 2: [], 3: [], 4: []}
        results_list = [Restaurant("woodstock", "pizza", 4, 4.5), Restaurant("flour house", "italian", 5, 5), Restaurant("the krusty krab", "burgers", 5, 5)]
        reps = {'flour house':1, 'the krusty krab':1, 'woodstock':1}
        result = main.results_sorting(results_list, reps)
        expected = {1: [Restaurant("woodstock", "pizza", 4, 4.5), Restaurant("flour house", "italian", 5, 5), Restaurant("the krusty krab", "burgers", 5, 5)], 2: [], 3: [], 4: []}
        self.assertEqual(result, expected)

    def test_results_sorting_2(self):
        results_list = [Restaurant("firestone", "barbecue", 4, 5),
                        Restaurant("flour house", "italian", 5, 5),
                        Restaurant("sally loo's", "cafe", 4, 5),
                        Restaurant("nite creamery", "dessert", 4, 5),
                        Restaurant("the krusty krab", "burgers", 5, 5),
                        Restaurant("cj's", "barbecue", 3, 4)]
        reps = {"firestone":2, "flour house":1, "sally loo's":1, "nite creamery":1, "the krusty krab":1, "cj's":1}
        expected = {1:[Restaurant("flour house", "italian", 5, 5),
                     Restaurant("sally loo's", "cafe", 4, 5),
                     Restaurant("nite creamery", "dessert", 4, 5),
                     Restaurant("the krusty krab", "burgers", 5, 5),
                     Restaurant("cj's", "barbecue", 3, 4)],
                  2:[Restaurant("firestone", "barbecue", 4, 5)],
                    3:[],
                    4:[]}
        result = results_sorting(results_list, reps)
        self.assertEqual(expected, result)


#Note that
    #def test_results_to_text_1(self):
       # matches = {1: [Restaurant("woodstock", "pizza", 4, 4.5), Restaurant("flour house", "italian", 5, 5), Restaurant("the krusty krab", "burgers", 5, 5)], 2: [], 3: [], 4: []}
        #result = results_to_text(matches[1], matches[2], matches[3], matches[4], "test.txt")


    #def test_results_to_text_2(self):
