#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What is you total bill?\n"))
people = int(input("How many people are splitting the bill?\n"))

bill_per_person = bill / people
tip = int(input("How much do you want to tip?\n")) / 100

pay = round(bill_per_person * tip + bill_per_person, 2)

print(f"Each person pays {pay}")