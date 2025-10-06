
print("What is your name?")
name = input()
print("How much is the amount to pay?")
money = int(input())

print("How much % you wanna leave for tip? 20% 22% 25%")
tip= int(input())
total = money + (money*tip)/100
print(name + " your total amount is:",total)