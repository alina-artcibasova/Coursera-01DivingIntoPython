#libraries
import sys

#grabbing input
step_string = sys.argv[1]
step_number = int(step_string)

#looping through the range
for number in range(1, step_number+1):
    print( ' '*(step_number - number) + '#'*number )