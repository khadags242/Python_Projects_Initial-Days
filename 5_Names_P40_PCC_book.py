# Share the names of a few of your friends in a list called names.Print each person's name by accessing each element in the list, once at a time

# defining a list of names
names = ["raghav", "shyam", "jadhav", "ghanshyam", "shamak"]

# print the list
print(f"\nThe elements of my list are {names}")

# accessing the elements of the list from the left
print("\nAccessing the list in natural orde")
print(f"\tThe first element in the lst is: {names[0].title()}")
print(f"\tThe second element in the list is: {names[1].title()}")
print(f"\tThe third element in the list is: {names[2].title()}")
print(f"\tThe fourth element in the list is: {names[3].title()}")
print(f"\tThe firth element in the list is: {names[4].title()}")

# accessing the elements of the list from the right
print("\nAccessing the list in reverse orde")
print(f"\tThe fifth element in the lst is: {names[-1].title()}")
print(f"\tThe fourth element in the list is: {names[-2].title()}")
print(f"\tThe third element in the list is: {names[-3].title()}")
print(f"\tThe second element in the list is: {names[-4].title()}")
print(f"\tThe first element in the list is: {names[-5].title()}")
