#libraries
import sys

#grabbing input
digit_string = sys.argv[1]

#making sum variable
sum = 0

#looping through the string
for symbol in digit_string:
    sum = sum + int(symbol)

#standard output
print(sum)