print("Marks And Grading Program")
print("Please Select the Class for Which You Want Add Marks:")
print("1. SSC \n2. HSC") 
mcls=int(input("\nEnter Your Choice:"))
if mcls == 1:
    print("You Choose SSC")
    print("\nPlease Enter The Marks Of Subject:")
    eng=int(input("Enter the Marks Of English Out of 150: "))
    urdu=int(input("Enter the Marks Of Urdu Out of 150: "))
    isl=int(input("Enter the Marks Of Islamiyat Out of 75: "))
    pst=int(input("Enter the Marks Of Pakistan Studies Out of 75: "))
    math=int(input("Enter the Marks Of Mathematics Out of 150: "))
    compsci=int(input("Enter the Marks Of Computer Science Out of 150: "))
    phy=int(input("Enter the Marks Of Physics Out of 150: "))
    chem=int(input("Enter the Marks Of Chemistry Out of 150: "))
    tmarks=eng+urdu+isl+pst+math+compsci+phy+chem
    percent=round((tmarks/1050)*100)
    if percent > 80:
        grade="A-1"
    elif (percent > 70) and (percent <=80):
        grade="A"
    elif (percent > 60) and (percent <=70):
        grade="B"
    elif (percent > 50) and (percent <=60):
        grade="C"
    else:
        grade="E"
    print("-----------------------------------------------")
    print("SUBJECTS         TOTAL MARKS     OBTAINED MARKS\n")
    print("ENGLISH              150                ",eng)
    print("URDU                 150                ",urdu)
    print("ISLAMIYAT            75                 ",isl)
    print("PAKISTAN STUDIES     75                 ",pst)
    print("COMPUTER SCIENCE     150                ",compsci)
    print("PHYSICS              150                ",phy)
    print("CHEMISTRY            150                ",chem)
    print("\nTOTAL               1050                ",tmarks)
    print("\nPERCNTAGE AND GRADE                     ",percent,grade)
    print("-----------------------------------------------")
elif mcls == 2:
    print("You Choose HSC")
    print("\nPlease Enter The Marks Of Subject:")
    eng=int(input("Enter the Marks Of English Out of 200: "))
    urdu=int(input("Enter the Marks Of Urdu Out of 200: "))
    isl=int(input("Enter the Marks Of Islamiyat Out of 50: "))
    pst=int(input("Enter the Marks Of Pakistan Studies Out of 50: "))
    math=int(input("Enter the Marks Of Mathematics Out of 200: "))
    compsci=int(input("Enter the Marks Of Computer Science Out of 200: "))
    phy=int(input("Enter the Marks Of Physics Out of 200: "))
    tmarks=eng+urdu+isl+pst+math+compsci+phy
    percent=round((tmarks/1100)*100)
    if percent > 80:
        grade="A-1"
    elif (percent > 70) and (percent <=80):
        grade="A"
    elif (percent > 60) and (percent <=70):
        grade="B"
    elif (percent > 50) and (percent <=60):
        grade="C"
    else:
        grade="E"
    print("-----------------------------------------------")
    print("SUBJECTS         TOTAL MARKS     OBTAINED MARKS\n")
    print("ENGLISH              200                ",eng)
    print("URDU                 200                ",urdu)
    print("ISLAMIYAT            50                 ",isl)
    print("PAKISTAN STUDIES     50                 ",pst)
    print("COMPUTER SCIENCE     200                ",compsci)
    print("PHYSICS              200                ",phy)
    print("\nTOTAL               1100                ",tmarks)
    print("\nPERCNTAGE AND GRADE                     ",percent,grade)
    print("-----------------------------------------------")
else:
     print("Please Try Again")