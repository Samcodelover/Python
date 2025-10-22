
import random
# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 100)
print(f"Random integer: {random_integer}")

for i in range(1, 5):
    print(f"{i} attempt:")
    first = int(input("Guess a number between 1 and 100: "))
    if first == random_integer:
        print(f"You guessed the number {first}!")
        break
    elif first > random_integer:
        print(f"Sorry, the number {first} is too high.")
    else:
        print(f"Sorry, the number {first} is too low.")



