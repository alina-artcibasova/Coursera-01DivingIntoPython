## ASSIGNMENT LINK
## https://www.coursera.org/learn/diving-in-python/programming/nc6Ce/key-value-khranilishchie
##
## USAGE
## saving value value with key key_name:
## $ storage.py --key key_name --val value
## retrieving value for key key_name:
## $ storage.py --key key_name
## if the key is already in the storage then new values do not rewrite old ones, but just added to storage
## retrieving values for such a key would return all the values
##
## EXAMPLE
## $ python storage.py --key key_name --val value
## $ python storage.py --key key_name
## value
## 
## $ python storage.py --key multi_key --val value1
## $ python storage.py --key multi_key --val value2
## $ python storage.py --key multi_key
## value1, value2
##
## If value for requested key hasn't been found, then return None

#importing libraries
import argparse # to parse command line arguments
import json # to store json files
import os #
import tempfile # file creation

parser = argparse.ArgumentParser(description='Storing key-value pairs.')
parser.add_argument('--key',
                    help='an integer for the accumulator')
parser.add_argument('--val',
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args)
