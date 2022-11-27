import get_ins 
'''
    This is the main file of the project. It will be the one that will be executed
    to run the program. It will be the one that will call the other files.

    The idea is to have a file that will be the one that will be executed to run
    the program. This file will be the one that will call the other files.
    The other files will be the ones that will contain the logic of the program.
'''

floats = get_ins.FloatRandoms(0, 100)

string = get_ins.StringRandom(max_length=10, min_length=10, content_type="just words", word_set=["cat", "dog", "chicken"])

boolean = get_ins.BooleanRandoms(format="letterL")

char = get_ins.CharacterRandoms()

integer = get_ins.IntegerRandoms(1,100,condition="x+3 <= 20 and x+3 >= 15")

print(string.get_random())
print(floats.get_random())
print(boolean.get_random())
print(char.get_random())
print(integer.get_random())

# x = get_ins.InputGenerator()