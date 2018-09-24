try:
    gross = int(input("What is your Gross Salary: "))
    children = int(input("How many children do you have: "))
except ValueError:
    print("Please enter a proper value.")
if gross<1000:
    tax = 0.1-(0.01*children)
elif gross<2000:
    tax = 0.12-(0.01*children)
elif gross<4000:
    tax = 0.14-(0.005*children)
else:
    tax = 0.18-(0.005*children)

net = gross*(1-tax)

print("Your net salary is:", net)

try:
    if gross<0 or children<0 or children>50:
        print("Invalid")
except ValueError
    print("Please enter a proper value.")
