# Name Cases- Store a person's name in a variable and then print that person's name in lower case, uppoer case & title case

user_name = input("Please neter your name: ")

user_name_lower = user_name.lower()
user_name_upper = user_name.upper()
user_name_title = user_name.title()

print(f"The original name was {user_name}")
print(f"\tThe name in lower case will be {user_name_lower}")
print(f"\tThe name in upper case will be {user_name_upper}")
print(f"\tThe name in title caase will be {user_name_title}")
