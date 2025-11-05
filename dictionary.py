print("Enter a text: !!")
text = input()
text = text.lower()
dict = {}
words = text.split()


for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)



