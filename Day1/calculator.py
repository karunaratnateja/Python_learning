a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

print("a:",a,"\nb:",b)

choice = input("Enter your choice:")

if choice == "+":
    print("Addition:",a+b)
elif choice == "-":
    print("subtraction",a-b)
elif choice == "*":
    print("Multiplication",a*b)
elif choice == "/":
    print("Division:",a/b)
else:
    print("invalid choice")