print("Mini Calculator")

numX = float(input("Enter the First Number: "))
numY = float(input("Enter the Second Number: "))

print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for square of the first number")


choice = int(input("Enter Your choice from 1-5: "))

if choice == 1:
    print("The Sum of two Numbers is", numX + numY)
elif choice == 2:
    print("The Subtraction of two Numbers is", numX - numY)
elif choice == 3:
    print("The Multiplication of two Numbers is", numX * numY)
elif choice == 4:
    print("The Division of two Numbers is", numX / numY)
elif choice == 5:
    num = float(input("Enter the number to square root: "))
    print("The Square of the first number is", num ** 2)

else:
    print("INVALID CHOICE")    