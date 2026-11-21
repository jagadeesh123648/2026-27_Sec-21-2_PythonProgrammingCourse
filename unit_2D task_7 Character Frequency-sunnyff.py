str1 = input("Enter a string: ")

freq = {}

for ch in str1:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:")

for ch in freq:
    print(ch, ":", freq[ch])