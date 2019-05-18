print("To Check Whether the Given Number Is Prime Or Not")
prinumb = int(input("Please Enter a Number:"))
for i in range(2,prinumb):
    if prinumb % i == 0:
        print("The Given Number:",prinumb,"Is Not a Prime Number")
        break
    else:
        print("The Given Number:",prinumb,"Is a Prime Number")
        break