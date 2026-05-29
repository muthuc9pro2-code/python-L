mobile = "7823995959"
masked = mobile[:2] + "****" + mobile[-2:]
print(masked)

song = "shape of you"
artist = "ed sheeran"
format = f"{song.title()} is a song by {artist.title()}."

print(format)

location = "chennai central"
fixed_location = location.replace("chennai central", "semabakkam")
print(fixed_location)

message = "your uber booking id is : UBER12345. Please keep it safe."
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)

# this seprating letters like , : ; etc are called delimiters

promo_msg = "use zomato100 to get 100 off on your first order"
if "zomato100" in promo_msg:
    print("offer applied")

feedback = "the food was great but the delivery was late"
print("position is :", feedback.split().index("great"))

feedback = "the food was great but the delivery was late"
print("position is :", feedback.find("great"))

name = "muthu kumar"
initials = "".join(word[0].upper() for word in name.split())
print(initials)

# for is a loop

dirty_string = "   airport  "
clean = dirty_string.strip()
print(clean)

word1 = "the trip was amazing and the car was clean"
wordCount = len(word1.split())
print(wordCount)

# strip() is nothing but to remove all spaces in the beginning and end of the string
