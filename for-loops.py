# FOR loops

# loop over lists
students = ["Karen", "Josh", "Peter", "Max", "Angela"]
for student in students:
    print(student)

# loop over lists with index
for index, student in enumerate(students):
    print(f"index: {index}, {student}")

# range(start, one after last, step): print even numbers from 0 to 10
for num in range(0, 11, 2):
    print(num)

# loop over a dictionary
hex_colors = {"white": "#FFF", "black": "#000", "gray": "#999"}
for label, hex_code in hex_colors.items():
    print(f"{label}:{hex_code}")

# continue & break keywords

names = ["Lucy", "Monica", "Alex", "Nina", "Jimmy"]
for name in names:
    if len(name) != 4:
        continue

    print(f"Hello, {name}")

    if name == "Nina":
        break

print("Done!")
