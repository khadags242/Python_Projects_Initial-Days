# You just found a bogger dinner table, so now more space os available. Think of three more guests to invite to Dinner.
# - Start with you program from 8_Changing_Guest_List_P46_PCCC.py . Add a print statment to the end of your program informing people that you found a bigger dinner table
# - Use insert() to add a new guest in the begining of your list
# - Use insert() to add one new guest to the middle of your list
# - Use append() to add one new guest to the end of your list
# - Print a new set of invitation messages, one for each person in your list

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

# Announcing that the guest number 3 (harpal) will not be able to make it
print(
    f"\nNews just in, {guest_list[2].title()} will not be able to join in. He will be replace by Khabri!!"
)

# updating the invite list
del guest_list[2]
guest_list.insert(2, "Khabri")

# printing the 2nd invite list
print("\nThe updated invite list")

print(f"\nInvitation for {guest_list[0].title()}")
print(f"\tWelcome to the party {guest_list[0].title()}")

print(f"\nInvitation for {guest_list[1].title()}")
print(f"\tWelcome to the party {guest_list[1].title()}")

print(f"\nInvitation for {guest_list[2].title()}")
print(f"\tWelcome to the party {guest_list[2].title()}")

print(f"\nInvitation for {guest_list[3].title()}")
print(f"\tWelcome to the party {guest_list[3].title()}")


# Announcing that a bigger space has been found and we will update the guest list to accomodate 3 more

print(
    f"\nNews just in, {guest_list[2].title()} will not be able to join in. He will be replace by Khabri!!"
)

# updating the invite list
guest_list.insert(0, "Makhii")
guest_list.insert(3, "sukhi")
guest_list.append("Haria")

# printing the 3nd invite list
print("\nThe updated invite list")

print(f"\nInvitation for {guest_list[0].title()}")
print(f"\tWelcome to the party {guest_list[0].title()}")

print(f"\nInvitation for {guest_list[1].title()}")
print(f"\tWelcome to the party {guest_list[1].title()}")

print(f"\nInvitation for {guest_list[2].title()}")
print(f"\tWelcome to the party {guest_list[2].title()}")

print(f"\nInvitation for {guest_list[3].title()}")
print(f"\tWelcome to the party {guest_list[3].title()}")

print(f"\nInvitation for {guest_list[4].title()}")
print(f"\tWelcome to the party {guest_list[4].title()}")

print(f"\nInvitation for {guest_list[5].title()}")
print(f"\tWelcome to the party {guest_list[5].title()}")

print(f"\nInvitation for {guest_list[6].title()}")
print(f"\tWelcome to the party {guest_list[6].title()}")
