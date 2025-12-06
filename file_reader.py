
filename = "text.txt"
list = []
def list_task(filename):

    with open(filename, "r") as f:
           for line in f:
                line = line.strip() #to get a clean line without '/n' we use strip()
                list.append(line)
    print(list)

#open and read the file after the appending:
def print_list():
    with open("text.txt") as f:
        print(f.read())


def add_task(task):
    with open("text.txt", "a") as f:
        f.write(task)

def delete_task(task):
    task_to_keep =[]

    with open("text.txt", "r") as f:

        for line in f:
            clean_line = line.strip()
        if clean_line.lower() != task.lower():
             task_to_keep.append(line)

    with open("text.txt", "w") as f:
        for kept_line in task_to_keep:
            f.write(kept_line)

    print(task_to_keep)




delete_task("bb")
list_task("text.txt")




