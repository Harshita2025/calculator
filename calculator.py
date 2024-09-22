#Simple Calculator that performs arithmetic operations.

print("Maths Calculator")

a = int(input("Enter the first number:\n"))

b = int(input("Enter the second number:\n"))

c = int(input("Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division \n"))

if c == 1:
  print("Sum of ",a , "and",b,"is", a+b)

elif c == 2:
  print("Difference ",a , "and",b,"is", a-b)

elif c == 3:
  print("Multiple of",a, "and",b,"is", a*b)

elif c == 4:
  print("Division of",a, "and",b,"is",a/b)

else:
  print("Invalid Button")
