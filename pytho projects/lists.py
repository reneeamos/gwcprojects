#remember: index numbers always start from zero
inventory = ["map", "house key", "canned food", "tent", "canned pineapple"]
print (inventory)
# to print one item at a time
print (inventory[0])
#to create a loop which will print all of the items at once (one at a time, per line)
for item in inventory:
    print (item)

# to get the size of a list (number of items) - len
print (len(inventory))

# to check if an item is in a list
print ("map" in inventory)
if ("map" in inventory):
    print ("you understand where you are now!")

# another way to print the items in a list by setting the length of the list to the range
# to get it to print the index number of each item on the list
# replace (inventory[item]) with (item)
# to get it to print the list formatted (the length of the list number of times)
# replace (inventory [item]) with (inventory)
for item in range(len(inventory)):
    print (inventory[item])




random = [inventory, "hello", 89.09, 98, True]
for item in random:
    print (item)

#both add to the ends of lists
#list.append - can add a list to a list or one element to a list
inventory.append("crackers")
print (inventory)

#list.extend - will merge the lists together, adding the individual elements
inventory.extend(["cheese", "parents"])
print (inventory)

#list.index


#lower - makes everything in the list lowercase


#isalpha - checks to see if list is only alphanumeric or not
