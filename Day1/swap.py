a = int(input("Enter your number:"))
b= int(input("Enter another number"))

print("="*20)

print("Swapping without a third variable")
print("Before Swapping:\n a:",a,"\n b:",b)
print("After Swapping:\n a:",b,"\n b:",a)


print("="*20)
print("Swapping with a third variable")
temp = a
a = b
b = temp
print("After Swapping:")
print("a:",a,"\nb:",b)