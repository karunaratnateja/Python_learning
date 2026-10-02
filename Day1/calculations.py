print("Enter marks for three subjects")

a = int(input("DMGT : "))
b = int(input("ADSA : "))
c = int(input("java : "))

total = a+b+c
avg = total/3

print("Total marks:",total)
print("Average marks:",avg)

print("="*16)

print("1.Celsius")
print("2.Fahrenheit")
choice = int(input("Enter your choice:"))

if choice == 1:
    C = int(input("Enter temperature in Celsius:"))
    F = ((c*9)/5)+32
    print("Temperature in fahrenheit:",F)
elif choice == 1:
    F = int(input("Enter temperature in Fanrenheit:"))
    C = (F-32)*5/9
    print("Temperature in Celsius:",C)
else:
    print("Invalid choice")

print("="*16)

p = int(input("Enter principal amount:"))
t = int(input("Enter your time:"))
r = int(input("Enter rate of intrest:"))

si = (p*t*r)/100
print("Simple Intrest:",si)