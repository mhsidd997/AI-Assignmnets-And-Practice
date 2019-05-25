'''Pyramid Pattern'''
for i in range(1,5):
    for j in range(5-i-1):
        print(end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print("\n")