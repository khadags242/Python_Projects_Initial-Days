# Find a quote by a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, "A person who never made a mistake never tried anything new.

name = input("Please enter the name of a famous person: ")
name_title = name.title()
quotation = input("Please enter the famous quote you would like to quote: ")
quotation_title = quotation.title()

print(f'{name_title} once said, "{quotation_title}"')
