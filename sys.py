import sys

if len(sys.argv) == 2:
    print("damal")
    sys.exit()
    
full_name = " ".join(sys.argv[1:])

email = full_name.replace(" ", ".").lower() + "@example.com"

print(full_name)
print(email)

# This is important concept for scheduling ,this sys.argv is nothing but take the value from terminal 
 
