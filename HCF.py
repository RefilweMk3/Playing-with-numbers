numberL = int(input("Enter the largest number: "))
numberS = int(input("Enter the smallest number: "))

while numberS:
    numStore = numberS
    numberS = numberL % numberS
    numberL = numStore
print("HCF is ",numberL)