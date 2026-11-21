
text = "  Hello Python Programming  "

print("Original String:", text)

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

print("Strip:", text.strip())

words = text.split()
print("Split:", words)
print("Join:", "-".join(words))

print("Replace:", text.replace("Python", "Java"))

print("Find:", text.find("Python"))