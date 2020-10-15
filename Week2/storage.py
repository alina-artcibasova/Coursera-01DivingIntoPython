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

parser = argparse.ArgumentParser(description='Program stores inputed key-value pairs in a file, or retrieves values for an inputed key.')
parser.add_argument('--key',
                    help='the key for the storage entry')
parser.add_argument('--val',
                    help='the value of a storage entry')
args = parser.parse_args()

#creating storage file path
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

# if key and value are supplied, we write them into file and print out nothing
if args.key and args.val:
    print('key and val condition')
    with open(storage_path, 'a') as f:
        f.write(json.dumps({args.key: args.val}, sort_keys=True, indent=4))
        print('written into file')
    
# if only key is supplied, we read the keys from a file and print out values corresponding to the key
if args.key and not args.val:
    print("key condition")
    with open(storage_path, 'r') as f:
        print(json.loads(f.read()))
