# dictionaries : store key value pair
# instead of maintaining two list of countries and population
# we can store together in a dictionary
# where country will be key (keys are always unique) and population will be value
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
print(world) # {'afghanistan': 30.55, 'albania': 2.77, 'algeria': 39.21}
print(type(world)) # dict
print(world["albania"]) # prints pop of albania
print(world.keys()) # prints all the keys

# check if key is present in the dictionary
print("albania" in world) # returns true if present
del(world["algeria"]) # deleted algeria from dict
print(world)

# adding or updating value
world["india"] = 55.57
world.update({"india": 55.68})
print(world)