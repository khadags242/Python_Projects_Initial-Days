# Think of at least 3 kinds of your favourite pizza. Store these pizza nanes in a list and then use a for loop to print the name of each pizza
# - Modify your for loop to print a sentance using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like "I like pepproni pizza"
# - Add a line at the end of your program, outside of the for loop, that states how much you like pizza. The output should consist of 3 or more lines about the kinds of pizza ypu like and then an additional sentence, such as I really love pizza

# Defining the pizza list
pizza_names = []
pizza_names.append("macaroni")
pizza_names.insert(1, "cheesy")
pizza_names.insert(2, "India")

# Printing the names of the pizzas from list
for pizza_name in pizza_names:
    print(pizza_name.title())

# Printing Pizza names with a sentence and not only names
for pizza_name in pizza_names:
    print(f"I love {pizza_name.title()}")

# Printing a final line after printing pizza names with a sentence

for pizza_name in pizza_names:
    print(f"I Love {pizza_name.title()}")

print("I really like all kinds of Pizza")
