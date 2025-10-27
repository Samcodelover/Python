
print("My ToDo list for today:")
list = []

for c in    range(1, 5) :
    print(f"{c} :")
    chore = input()

    if chore == "stop" :
        break
    if chore == "delete" :
        print("put the list number which you wanna delete:")
        i = int(input())
        list.pop(i)

    if chore == "view" :
        print("my to do list:")
        print(list)
    else:
        list.append(chore)






