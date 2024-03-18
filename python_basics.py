# Addition
print("2 + 2 =",2+2)

# Subtraction
print("2 - 2 =",2-2)

# Multiplication
print("2 8 2 =",22)

# Division
print("2 / 2 =",2/2)

# Variable : case sensitive
height = 1.79
weight = 68.7
bmi = weight / height ** 2  # ** means power of
print(bmi)

# data types
print(type(1))
print(type(1.1))
print(type(True))
print(type("hello"))

# Type conversion
age = 21
# str can only be concatenated with another str. so we converted int to str
print("My name is shivansh kush, i am " + str(age) + " years old.")
float_str = "1.11"
float_actual = float(float_str)

print("I said " + ("Hey " * 2) + "Hey!")

# List
names = ["smith", "john", "doe"]
print(names)
print(type(names))

# list of lists
weights = [["smith", 60], ["john", 50], ["doe", 67]]
print(weights)

# accessing elements using index
print(weights[0]) # first element
print(weights[-1]) # last element

# slicing
characters = ['a', 'b', 'c', 'd', 'e', 'f']
print(characters[2:5]) # index 2 to 5 where 2 is inclusive and 5 is exclusive
print(characters[:5]) # 0 index to 4
print(characters[2:]) # index 2 to end

# list manipulation
characters[1] = 'h'
print(characters)
characters[:2] = ['a', 'b']
print(characters)
characters  = characters + ['g']
print(characters)

# deleting element
del(characters[1])
print(characters)

# If we create a new list y using x and we make any changes to y then it will be reflected to x as it is a reference to same list
x = ['a', 'b', 'c']
y = x
y[1] = 1
print(y)
print(x)

# in order to make a seperate list entirely
# we can either use list function or use slicing
y = list(x)
y = x[:]

# functions
print(max([1, 2, 3, 4])) # inbuilt max function
print(round(1.6)) # inbuilt round function
print(round(1.67, 1));
print(len("abc"))

# sort function
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second
full_sorted = sorted(full, reverse=True)
print(full_sorted)

# Methods : functions that belong to objects
# every datatype is an object
fam = ['liz', 'emma', 'smith', 'smith']
print(fam.index('emma')) # gets the index of parameter
print(fam.count("smith")) # returns count of parameter

lower = "abc"
print(lower.capitalize())
print(lower.upper())
print(lower.lower())
print(lower.replace('c', 'd'))

fam.append("john")
print(fam)