arr = [1,20,300,400, 500]
target = 520
new = []
for i in arr:
    for j in arr:
        if i + j == target:
            new.append(arr.index(i))
print(new)