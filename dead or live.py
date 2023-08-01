text = input()

# count the number of occurrences of ":)" and ":("
smiley_count = text.count(":)")
frowny_count = text.count(":(")

if smiley_count > 0 and frowny_count == 0:
    print("alive")
elif smiley_count == 0 and frowny_count > 0:
    print("undead")
elif smiley_count > 0 and frowny_count > 0:
    print("double agent")
else:
    print("machine")

