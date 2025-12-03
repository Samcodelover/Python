
def add_task():
    list = []
    with open("text.txt", "r") as f:
        for c in f:

            list.append(c.strip())


#open and read the file after the appending:
def print_list():
    with open("text.txt") as f:
        print(f.read())





add_task()
print_list()