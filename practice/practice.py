# practice

names = ["muthu", "kumar", "suresh", "rajesh", "vijay"]

for name in names:
    print(name.upper())

names = ["muthu", "suresh", "saravanan", "kumar", "selva"]

for name in names:
    if name.startswith("s"):
        print(name)

count = 0

for name in names:
    if name.startswith("s"):
        count += 1
print("Number of names starting with s :", count)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in num:
    if n%2 == 0:
        print(n)

number = [10, 5, 40, 25, 8, 3]

largest_num = 0

for num in number:
    if num > largest_num:
        largest_num = num
print(largest_num)

largest = number[0]

for num in number:
    if num > largest:
        largest = num 
print(largest)

largest = max(number)
print(largest)

names = ["muthu", "kumar", "suresh"]

capitalized_names = []

for name in names:
    capitalized_names.append(name.capitalize())
print(capitalized_names)

capitalized_names = [name.capitalize() for name in names]

print(capitalized_names)

# str's  are immutable so change it and change the changed value for the previous str

prices = [100, 250, 300, 150]

total = 0

for num in prices:
    total += num
print(total)

playList = ["song1", "song1", "song3", "song4", "song5", "song4"]

for song in set(playList):
    if playList.count(song) >= 2 :
        print(song)

foods = ["pizza", "burger", "ice cream", "pasta"]

longest = ""

for food in foods:
    if len(food) > len(longest):
        longest = food
print(longest)

reversed_foods = [food[::-1] for food in foods]
print(reversed_foods)








