trip = {
    "destination": "Paris",
    "duration": 7,
    "activities": ["sightseeing", "museum visits", "cafe hopping"],
    "budget": 1500.00,
    "driver": "ravi",
    "status": "planned",
    "destination": "london",
}

print(trip["destination"])

# reading the key is called lookUp the above code is a lookUp example

print(trip.get("duration"))

# get is also used to lookUp the value of the key, we use get() to avoid the error if the key is not present in the dictionary it will return None instead of throwing an error so our code will not be killed

print(trip.keys())
print(trip.values())

# to get keys and values we can use keys() and values() method respectively

for i, n in trip.items():
    print(f"{i} : {n}")

print(trip.get("activities")[1])

# like js object dictionaries can have more than one value for a a key by using list

trip.update({"poda": "potta"})
print(trip)

trip.update({"poda": "nallavan"})
print(trip)

trip.pop("poda")
print(trip)

# update in dictionary will add the key if that key is not exist and if the key is exist then it will update the value of the key
# pop is used to remove the last added key and value pair

for i, n in trip.items():
    print(f"{i} : {n}")

# dictionary will not allow duplicate keys it will only keep the lastest key of same name

for activity in trip.get("activities"):
    print(activity)

# you can also iterate through the list of values in the dictionary by using get() method to access the list and then iterate through it using a for loop.
# we cant have dictionary inside a dictionary without a key becausse dictionary only take key, value pair ypu can only have tuples inside the list

damal = [
    {
        "destination": "Paris",
        "duration": 7,
        "activities": ["sightseeing", "museum visits", "cafe hopping"],
        "budget": 1500.00,
        "driver": "ravi",
        "status": "planned",
    },
    {
        "destination": "london",
        "duration": 5,
        "activities": ["sightseeing", "museum visits", "cafe hopping"],
        "budget": 1200.00,
        "driver": "ravi",
        "status": "planned",
    },
]

for i, n in damal[1].items():
    print(f"{i} : {n}")

damal = {
    "trip1": {
        "destination": "Paris",
        "duration": 7,
        "activities": ["sightseeing", "museum visits", "cafe hopping"],
        "budget": 1500.00,
        "driver": "ravi",
        "status": "planned",
    },
    "trip2": {
        "destination": "london",
        "duration": 5,
        "activities": ["sightseeing", "museum visits", "cafe hopping"],
        "budget": 1200.00,
        "driver": "ravi",
        "status": "planned",
    }
}

# we can add dictionary inside a dictionary by using a key for the inner dictionary as shown above

for i, n in damal.items():
    print(i)
    print(n.get("destination"), "--->" ,n.get("duration"))
