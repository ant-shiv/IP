def circle(r):
  return 3.14*r*r
def square(a):
  return a*a
def rectangle(l,b):
  return l*b

print("1 to calculate Area of circle [A=πr2]")
print("2 to calculate Area of square [A=a*a]")
print("3 to calculate Area of rectangle [A=l*b]")

n=int(input("Enter your Choice(1,2,3): "))
if n==1:
 r=float(input("Enter value of r:"))
 A=circle(r)
 print("Area of circle is ",A)
elif n==2:
  a=float(input("Enter value of a:"))
  A=square(a)
  print("Area of square is ",A)
elif n==3:
    l=float(input("Enter value of l:"))
    b=float(input("Enter value of b:"))
    A=rectangle(l,b)
    print("Area of rectangle is ",A)
else:
 print("Your choice is Wrong")
