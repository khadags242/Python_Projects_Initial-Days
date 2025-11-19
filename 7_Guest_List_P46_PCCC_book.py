# If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least 3 people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner

# defining the list
guest_list = []

# feeding the list with invitee's names
guest_list.insert(0, "kashu")
guest_list.insert(1, "madhav")
guest_list.insert(2, "harpal")
guest_list.insert(3, "kuber")

# printing the 1st invite list

print(f"\nInvitation for {guest_list[0].title()}")
print(f"\tWelcome to the party {guest_list[0].title()}")

print(f"\nInvitation for {guest_list[1].title()}")
print(f"\tWelcome to the party {guest_list[1].title()}")

print(f"\nInvitation for {guest_list[2].title()}")
print(f"\tWelcome to the party {guest_list[2].title()}")

print(f"\nInvitation for {guest_list[3].title()}")
print(f"\tWelcome to the party {guest_list[3].title()}")
