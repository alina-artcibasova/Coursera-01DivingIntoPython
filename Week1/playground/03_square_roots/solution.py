#libraries
import sys

#inputs
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

#computing determinant
D = b**2 - 4*a*c

#computing roots
x1 = ( -b + (D)**0.5 ) / (2*a)
x2 = ( -b - (D)**0.5 ) / (2*a)

# outputting roots
print(int(x1))
print(int(x2))