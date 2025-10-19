
print("What is the guest's name?")
name = input()
print("How many people in their group?")
people = int(input())
print("How much is the amount to pay?")
money = int(input())

print("How much % you wanna leave for tip? 20% 22% 25%")
tip= int(input())
total = money + (money*tip)/100
print(name + " the total amount for your group is:",total)

pay = total/people
print("How much each person in the group will pay including tips?", pay)

if(tip > 20):
    print("Thank you for your generosity!")

