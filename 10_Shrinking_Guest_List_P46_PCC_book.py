# You just found out that your new dinner table wasnt arriving in time for the dinner and you have spcae for only two guest
# - Start with your program from the excercise 8_Changing Guest_list_P46_PCCC_book.py
# - Use pop() to remove guests from your list one at a time until only 2 names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you'r sorry you can't invite them to dinner
# - print a message to each of the two people still on your list, letting them know they're still invited
# - use del to remove the last two names from your list, so that you have an empty list. Print your list to make sure you actually have an empty list at the end of your program

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

# Shrinking the guest list again
print(
    "\njust got to know that the bigger dinner table is not availble, we can invite only 2 people"
)

deleted_guest0 = guest_list.pop(0)
print(
    f"My apologies {deleted_guest0.title()} but we will have to cancel your invite for this time"
)



deleted_guest1 = guest_list.pop(1)
print(f"My apologies {deleted_guest1.title()} but we will have to cancel your invite for this time")

# printing the 3nd invite list
print("\nThe updated invite list")

print(f"\nInvitation for {guest_list[0].title()}")
print(
   f"\tDear {guest_list[0].title()}, we are pleased to invite to finally to our dinner"
 )

print(f"\nInvitation for {guest_list[1].title()}")
print(
   f"\tDear {guest_list[1].title()}, we are pleased to invite to finally to our dinner"
)

#print(guest_list)

# Final deletion of the names from the list
del guest_list[0]
del guest_list[0]

print(f"\nThe final guest list after all deletions is empty {guest_list}")
