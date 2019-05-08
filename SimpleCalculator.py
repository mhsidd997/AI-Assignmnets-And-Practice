print("Simple Calculator")
print("\nEnter Two Number For Calulation\n")
a=float(input("Enter First Number:"))
b=float(input('Enter Second Number:'))
c=input("\nSelect Operation: +, -, *, / : ")
if c == '+':
    print("\nSum is:",a+b)
elif c == '-':
    print("\nDifference is:",a-b)
elif c == '*':
    print("\nProduct is:",a*b)
elif c == '/':
    print("\nDivision is:",a/b)
else:
    print("\nInvalid Opration")