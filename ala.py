import timeit

print(timeit.repeat(stmt="random.randint(0, 50)", setup ="import random", repeat = 4))
