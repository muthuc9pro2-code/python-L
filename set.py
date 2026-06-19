# set is unordered collection of items its mutable and it just eliminate the duplicates it is defined by {}

a = {1, 2, 3, 4, 5}
print(a)  # Sets are unordered, so indexing is not possible

# dictionaries and set are defined by using {} but the difference is that dictionaries have key and value pairs 

# we can also change the set to list and vice versa by set() and list() respectively

uber_city = ["chennai", "bangalore", "bangalore", "mumbai", "delhi", "kolkata"]
unique_cites = set(uber_city)
print(unique_cites)

uber_city1 = {"chennai", "bangalore", "bangalore", "mumbai", "delhi", "kolkata"}
uber_city2 = {"seattle", "san francisco", "new york", "chicago", "boston", "chennai", "bangalore"}

print(uber_city1.union(uber_city2)) 
print(uber_city1.intersection(uber_city2))
print(uber_city1.difference(uber_city2))

# set can be used to perform set operations like union, intersection and difference etc 
# set is mutable but it can only add or remove but not replace or update the existing element in the set

uber_city1.add("hyderabad")
print(uber_city1)

uber_city1.remove("mumbai")
print(uber_city1)

# you can only replace by add and remove in set





