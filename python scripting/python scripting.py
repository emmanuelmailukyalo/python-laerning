# zip 

from tokenize import Number


fruits = {
            'pears':1,
            'peaches':1,
            'grapes':1,
            'bananas':1,
            'apples': 4,
            'oranges': 19,
            'kites': 3,
            'sandwiches': 8
         }

name, size  = zip(*fruits)
print(name)
