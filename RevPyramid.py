'''Reverse Pyramid Pattern'''
for i in range(6,0,-1):
    for j in range(0,6-i):
        print(end=' ')
    for j in range(0,i):
        print("*",end=' ')
    print("\n")