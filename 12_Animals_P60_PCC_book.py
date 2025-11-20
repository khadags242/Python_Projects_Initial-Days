# Think of a list of 3 different animals that have a common charecteristics. Store the name of these animals in a list and then use a for loop to print out the name of each animal
# Modify your program to print a statement about each animal such as "a Dog would make a great pet"
# Add a line at the end of your program stating what these animals have in common. You could print a sentence such as "Any of these animals will make a great pet"

# creating a list of animals

animals = []
animals.insert(0, "dog")
animals.insert(1, "cat")
animals.insert(2, "cow")

# printing the name of the animals using a for loop
for animal in animals:
    print(animal.title())

# instead of just name, print a statement about each animal
for animal in animals:
    print(f"A {animal.title()} would make a great pet")

# after pringting one line for each animal, print a statement in wgat these animals has in common
for animal in animals:
    print(f"A {animal.title()} would make a great pet")
print("Any of these anumals will make a great pet")
