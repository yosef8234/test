# Q:
# Given the following subclass of dictionary:

class DefaultDict(dict):
  def __missing__(self, key):
    return []

# Will the code below work? Why or why not?

d = DefaultDict()
d['florp'] = 127

# A:

# Yes, it will work. With this implementation of the DefaultDict class, whenever a key is missing, the instance of the dictionary will automatically be instantiated with a list.

# >>> d
# {'florp': 127}
