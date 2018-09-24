a = int(input("Please input your number: "))
tempa = a
b = 0
while a > 0:
    b = 10*b + (a%10)
    a= a//10
    if tempa==b:
        print("Your number is a palindrome!!")