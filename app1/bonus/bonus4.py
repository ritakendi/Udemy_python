from bonus.parsers4 import parse
from bonus.coverter4 import convert
feet_inches = input("Enter feet and inches: ")


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
