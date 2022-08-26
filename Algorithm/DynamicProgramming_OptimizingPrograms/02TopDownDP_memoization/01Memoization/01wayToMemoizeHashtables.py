dictionary = {}

key = 1
value = "abcd"

# To add value against a key in the dictionary, do this

dictionary[key] = value
#or
dictionary[2] = 'abc'

# keys and values can be anything, from integers to strings to custom objects

dictionary['hello'] = 'hi'
dictionary[1.1] = 1

class Dummy:
    def __init__(self, val):
        self.val = val
        
customObject = Dummy(5)
dictionary[customObject] = 5

# To iterate over dictionary do this
for k,v in dictionary.items():
    print(k, ":", v)