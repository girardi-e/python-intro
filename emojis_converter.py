# ask user to enter a message containing an emoji
message = input(">")

# divide message up into separate words
words = message.split(" ")

# map emojis inside a dictionary
emojis = {
    "=)": "😃",
    "=(": "☹️ "
}

# loop over words and see if they match the keys inside emojis
output = ""

for word in words:
    # .get(keyname, value(optional - return this if key does not exist))
    output += emojis.get(word, word) + " "

print(output)
