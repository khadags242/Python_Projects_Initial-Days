# You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite
# - Start with your program from 6_Guest_List_P46_PCCC_book.py. Add a print statment at the end of your program stating the name of the guest who can't make it
# - Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting
# - Print a second set of invitation messages, one for each person who is still in your list

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
