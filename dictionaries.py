# It is best to think of a dictionary as a set of key: value pairs,
# with the requirement that the keys are unique (within one dictionary).
# A pair of braces creates an empty dictionary: {}.

# create an empty dictionary
empty_dict = {}
another_empty_dict = dict()
print(type(empty_dict))


month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# access keys and values
print(month_conversions["Jan"])
print(month_conversions.get("Dec"))

# provide a default value
print(month_conversions.get("Luv", "Not a valid key"))

# adding key-value pair
month_conversions["Vac"] = "Vacation"

# delete key-value pair
del month_conversions["Sep"]

# join two dictionaries
christmas = {"X-mas": "Christmas"}
month_conversions.update(christmas)

# sort a dictionary
sorted(month_conversions)

# convert a dictionary into a list
# list(month_conversions)

# look for a key
print("Aug" in month_conversions)

# get all the keys and values: returns a list of  tuples
month_conversions.items()

# Looping through dictionaries
for key, value in month_conversions.items():
    print(key, value)

# storing values in a list
students = {
    "Robert Garcia": [32, "male", 3.7],
    "Sonia Blade": [35, "female", 4.0]
}

students["Robert Garcia"].append("martial arts")

print(students.items())
