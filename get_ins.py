"""
Generates random inputs from given parameters as input.

Made by:    {  'Ceballos Alonso Laura Valentina', 
                'Díaz Medina César Esteban', 
                'Silva Capera Daniel Santiago'
            }
"""

# ? Usually in prgramming contests, the first parameter given as input is
# ? the ammount of test cases.
# ? The options could be: None, one, a finite number of tests or undifined number of tests

import itertools
import random
import string


class FormatInput:
    list_formats = {
        "separator": " ",
        "end": "",
    }
    parameters_format = {
        "begin": "",
        "end": "",
        "separator": " ",
    }
    input_types = {  #! For now just uncommented the ones that are already implemented
        # "Blank",
        "Any",
        "Next Line",
        "Integer",  # * Class Done
        "Float",  # * Class Done
        "String",  # * Class Done
        "Character",  # * Class Done
        "Boolean",  # * Class Done
        "List",
        # "Tuple",
        # "Set",
        # "Dictionary",
        # "Array",
        # "Matrix",
        # "Graph",
        # "Tree",
        # "Binary Tree",
        # "Binary Search Tree",
        # "Heap",
        # "Stack",
        # "Queue",
        # "Linked List",
        # "Doubly Linked List",
        # "Circular Linked List",
        # "Circular Doubly Linked List",
        # "Hash Table",
        # "Trie",
        # "Directed Graph",
        # "Undirected Graph",
        # "Weighted Graph",
        # "Directed Weighted Graph",
        # "Undirected Weighted Graph",
        # "Directed Acyclic Graph",
        # "Undirected Acyclic Graph",
        # "Directed Acyclic Weighted Graph",
        # "Undirected Acyclic Weighted Graph",
        # "Directed Cyclic Graph",
        # "Undirected Cyclic Graph",
        # "Directed Cyclic Weighted Graph",
        # "Undirected Cyclic Weighted Graph",
        # "Binary Search Tree",
        # "Binary Search Tree with Duplicate Keys",
        # "Binary Search Tree with Duplicate Keys and Parent Pointers",
        # "Binary Search Tree with Parent Pointers",
        # "Binary Search Tree with Parent Pointers and Duplicate Keys",
    }

    def __init__(
        self, ins: list, parameters_format: dict = parameters_format
    ):  # ,condition):
        # ? The ins list should be seen like this: [Integer, Integer, Float, List]
        # ? By default, the list will be separated by spaces 'Integer Integer Float List'
        # ? for an input with 4 parameters, the first one is an integer,
        # ? the second one is an integer,
        # ? the third one is a float and the fourth one is a list.
        # ? The generator will output a list like this [1, 2, 3.0, [1,2,3,4,5]]
        # ? The list will be separated by spaces '1 2 3.0 [1,2,3,4,5]'
        # ? The lists and matrices can have its own format given by the user.

        '''

2 5 4
1 2

Integer(,condition='x%2==0') Integer Integer nextLine List(type=(Integer(,condition='x%2==0')),length_type=fixed,max_length=1e3)


        '''

        raise NotImplementedError


class IntegerRandoms:
    def __init__(self, min_n, max_n, condition: str = "True", variable:str='x'): #! Pending to write variable names
        self.min_n = min_n
        self.max_n = max_n
        self.condition = condition

    def get_random(self):
        return next(
            x
            for x in map(
                lambda x: random.randint(self.min_n, self.max_n) | 1, itertools.count()
            )
            if eval(self.condition)
        )


class FloatRandoms:
    def __init__(self, min_n, max_n, condition: str = "True", format: int = 2):
        self.min_n = min_n
        self.max_n = max_n
        self.condition = condition
        self.format = format

    def get_random(self):
        ##! return a random float number with *format* decimals

        return next(
            x
            for x in map(
                lambda x: random.uniform(self.min_n, self.max_n), itertools.count()
            )
            if eval(self.condition)
        )


class CharacterRandoms:
    def __init__(self, min_n: int = 97, max_n: int = 122, condition: str = ""):
        self.min_n = min_n  #! ASCII code
        self.max_n = max_n  #! ASCII code
        if condition == "" or condition == "None" or condition == "Unrestricted":
            self.condition = "True"
        else:
            self.condition = condition

    def get_random(self):
        return next(
            x
            for x in map(
                lambda x: chr(random.randint(self.min_n, self.max_n)), itertools.count()
            )
            if eval(self.condition)
        )


class BooleanRandoms:
    bool_formats = {
        "nums",
        "lettersUCC",
        "lettersL",
        "lettersU",
    }
    bools = {
        1: "True",
        0: "False",
    }

    def __init__(self, format: str = ""):
        self.format = format

    def getRandomBool(self):
        bool_value = random.randint(0, 1)
        if self.format == "lettersUCC":
            return self.bools[bool_value].upper()
        elif self.format == "lettersL":
            return self.bools[bool_value].lower()
        elif self.format == "lettersU":
            return self.bools[bool_value].capitalize()
        return self.bools[bool_value]


class StringRandom:
    content_types = {  #! For now just uncommented the ones that are already implemented
        # 'mixed nums and letters UCC',
        # 'mixed nums and letters L',
        # 'mixed nums and letters U',
        # "nums",
        "letters english",
        # 'letters UCC',
        # 'letters L',
        # 'letters U',
        # 'special chars',
        # 'special chars UCC',
        # 'special chars L',
        # 'special chars U',
        # 'special chars and nums',
        # 'special chars and nums UCC',
        # 'special chars and nums L',
        # 'special chars and nums U',
        "random",
        "mixed with words",
        "just words",
    }

    def __init__(
        self,
        content_type: str = "random",
        min_length: int = 1,
        max_length: int = 10,
        word_set: list = [],
        condition: str = "",
    ):
        self.min_length = min_length
        self.max_length = max_length
        self.word_set = word_set
        self.content_type = content_type
        if condition == "" or condition == "None" or condition == "Unrestricted":
            self.condition = "True"
        else:
            self.condition = condition

    def get_random(self):
        if self.word_set and self.content_type == "just words":
            return "".join(random.choice(self.word_set))
        elif self.word_set and self.content_type == "mixed with words":
            word_or_random = random.randint(0, 1)  # ? 0 for random, 1 for word
            if word_or_random:
                return "".join(random.choice(self.word_set))
            else:
                res = "".join(
                    random.choices(
                        string.ascii_lowercase + string.digits,
                        k=random.randint(self.min_length, self.max_length),
                    )
                )

                return res
        elif self.content_type == "letters english":
            res = "".join(
                random.choices(
                    string.ascii_lowercase,
                    k=random.randint(self.min_length, self.max_length),
                )
            )

            return res
        else:
            res = "".join(
                random.choices(
                    string.ascii_lowercase + string.digits,
                    k=random.randint(self.min_length, self.max_length),
                )
                if eval(self.condition)
                else self.get_random()
            )

            return res


class ListRandom:

    content_types = FormatInput.input_types

    def __init__(
        self,
        length_type: str = "fixed",
        min_length: int = 1,
        max_length: int = 10,
        content_type: str = "Any",
    ):
        if length_type == "fixed":
            self.min_length = max_length
        else:
            self.min_length = min_length
        self.max_length = max_length

        self.length = random.randint(self.min_length, self.max_length)
        self.content_type = content_type

    def get_random(self):
        if self.content_type == "Any":
            print("hey")
            #!for each element of list (min, max), request content_type
        # else:
        #     for i in range(self.ength):


# class DataList:

#     content_types = FormatInput.input_types

#     def __init__(
#         self,
#     ):


class InputGenerator:
    Input_Generator_type = None
    test_cases_options = {
        0: "None",
        1: "Single One",
        2: "Finite Number",
        3: "Undefined Number",
    }

    def __init__(self, test_cases=None):
        self.test_cases = test_cases
        print(
            """Your problem, from each execution, how many times will request the same inputs?
        Select one
            """
        )
        for test_opt in self.test_cases_options:
            print(test_opt, "", self.test_cases_options[test_opt])

        not_valid_option = True

        while not_valid_option:
            try:
                option = int(input("Option: "))
                if option in self.test_cases_options:
                    not_valid_option = False
                else:
                    print("Oops!  That was no valid number.  Try again...")
            except:
                print("Oops!  That was no valid number.  Try again...")

        selected_option = self.test_cases_options[option]

        print("You selected: ", selected_option)

        self.Input_Generator_type = option

    def get_input(self):
        if self.Input_Generator_type == 0:
            return None
        elif self.Input_Generator_type == 1:
            return self.get_single_input()
        elif self.Input_Generator_type == 2:
            return self.get_finite_input()
        elif self.Input_Generator_type == 3:
            return self.get_undefined_input()
