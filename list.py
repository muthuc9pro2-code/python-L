favourite_food = ["pizza", "burger", "sushi", "pasta", "ice cream"]
playList = ["song1", "song2", "song3", "song4", "song5"]
recent_locations = ["beach", "mountains", "city", "countryside", "desert"]

"""
print("zomato foods :", favourite_food)
print("playlist :", playList)
print("recent locations :", recent_locations)
"""

# list can have multiple data types like js

playList.append("song6")
print("playList :", playList)

playList.insert(2, "song7")
print("playList :", playList)

playList.remove("song7")
print("playList :", playList)

playList.pop()
print("playList :", playList)

# pop is just like remove but only removes the last element 

playList.pop(1)
print("playList :", playList)

# if pop has an index it removes the element at that index otherwise it removes the last element

playList.reverse()
print("playList :", playList)

# reverse is used to reverse the order of the list elements

print("length of playList :", len(playList))

print("count", playList.count("song1"))

# count is nothing but the number of times an element appears in the list

# List_Slicing

print("top 2 songs :", playList[0:2])
print("Last 2 songs :", playList[-2:])
print("Wanted songs :", playList[2:4])
print("wanted songs :", playList[2])

# the above code is to slice the list , it uses : to get more than one element and it uses - to get the last elements of the list

# List_Iteration

for food in favourite_food:
    print(food)

for song in playList:
    print(song+ " by  michael jackson")

# list is mutabale but string is immutable 

list = ["muthu", "kumar", "suresh"]

list[0] = "koki"
print(list)

for i,place in enumerate(recent_locations):
    print(f"{i} : {place}")








