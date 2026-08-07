# Dictionaries - A collection (array) of {key:value} pairs ordered and chanageable. NO duplicates

# A dictionary is one of the four basic types of collections for jr. devs
# Enclose the dic_name{} with a set of curly braces like a set{}
capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Ukraine":"Kyiv"}

# To see all of the possible attributes and methods for dic_name{} use the directory method dir(dic_name)
# To get an in-dpeth description of each use the help mthod help(dic_name)
# print(dir(capitals))
# print(help(capitals))

# The follwoing are a few methods available to dic{}:
# The .get(value) method parses a dictionary for a given value
print(capitals.get("USA"))  # Prints "Wahsington D.C."

# If no values are found, the method would return None, which can be used in an if-statement
# It can be treated as an off state (or a boolean for False)
if capitals.get("Japan"):   # Prints "That capital is NOT in our dictionary"
    print("That capital is in our dictionary")
else:
    print("That capital is NOT in our dictionary")
print()

# The .update({value}:{value}) method can add values to our dictionary using the same syntax for initializing the dictionary
capitals.update({"Germany":"Berlin"})
print(capitals) # Prints {..., 'Germany': 'Berlin'}

# the .update() method can also be used to update preexisting values
capitals.update({"USA":"Detriot"})
print(capitals) # Prints {..., 'USA': 'Detriot'}

# The .pop("{key}") method can remove specific values from the dictionary via a key (like an index/element)
capitals.pop("USA")
print(capitals) # Prints "{'India': 'New Delhi', 'China': 'Beijing', 'Ukraine': 'Kyiv', 'Germany': 'Berlin'}"

# The .popitem() method will remove the latest key value that was inserted
capitals.popitem()
print(capitals) # Prints "{'India': 'New Delhi', 'China': 'Beijing', 'Ukraine': 'Kyiv'}"
print()
# The .clear() method will truncate all keys from the dictionary
# capitals.clear()
# print(capitals) # Prints "{}"

# The .keys() method will return all of the keys (i.e., indices) from a dictionary
# Technically, keys is an object that resembles a lists
keys = capitals.keys()
print(keys)     # Prints object "dict_keys(['India', 'China', 'Ukraine'])"

# This is iterable like w/index values
for key in keys:
    print(key)  # Prints "India China Ukraine" on newlines
print()

# the .values() method will return all of the values (i.e., element values) from a dictionary
values = capitals.values()
print(values)   # Prints object "dict_values(['New Delhi', 'Beijing', 'Kyiv'])"

for value in values:
    print(value)    # Prints "New Delhi Beijing Kyiv" on newlines
print()

# The .items() method will return a dictionary object that resembles a 2D list
items = capitals.items()
print(items)    # Prints object "dict_items([('India', 'New Delhi'), ('China', 'Beijing'), ('Ukraine', 'Kyiv')])"

# Can iterate like you would with a 2D lis
for key, value in items:
    print(f"{key}: {value}")    # Prints key-value pairs on newlines
print()