#Write a subroutine that outputs the following properties of a circle from the the diameter and arc angle.
D = int(input("What is the diameter? "))
AA =int(input("What is the arc angle? "))



#Subroutine to find the area and circumference of the circle
def Properties(X):
  return (X * 3.14)

#Main Programme
R = D / 2
A = round(Properties(R ** 2),3)
C = round(Properties(D),3)
AL = round((C * AA) / 360,3)
print("The radius is", R)
print("The area is", A)
print("The circumference is", C)
print("The arc length is", AL)