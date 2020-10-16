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
## EXAMPLES
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
##
#############################
## TESTS
#############################
## $ python storage.py --key key_name --val value
## $ python storage.py --key key_name
## value
## 
## $ python storage.py --key multi_key --val value1
## $ python storage.py --key multi_key --val value2
## $ python storage.py --key multi_key
## value1, value2
## 
## $ python storage.py --key key_fake
## None

#############################
## LIBRARIES
#############################
import argparse # to parse command line arguments
import json # to store json files
import os #
import tempfile # file creation

#############################
## ARGUMENT PARSER
#############################
parser = argparse.ArgumentParser(description='Program stores inputed key-value pairs in a file, or retrieves values for an inputed key.')
parser.add_argument('--key',
                    help='the key for the storage entry')
parser.add_argument('--val',
                    help='the value of a storage entry')
args = parser.parse_args()

#############################
## WRITING INTO THE STORAGE
#############################
#creating storage file path
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

# if key and value are supplied, we write them into file and print out nothing
if args.key and args.val:
    
    #reading storage file
    #if it exists we load the data from it into saved_data
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            saved_data = json.load(f)
    #if it doesn't exist, we set it to hold an empty dictionary
    else:
        saved_data = json.loads('{}')
        #print('saved data:\n', saved_data)
    
    #updating the storage
    #if key is already present in the file, then we append the value string to it
    if args.key in saved_data.keys():
        saved_data.update({args.key: saved_data[args.key]+', '+args.val})
    #if not, we just create a new entry
    else:
        saved_data.update({args.key: args.val})
        #print('updated data:\n', saved_data)
    
    #writing updated dictionary into file
    with open(storage_path, 'w') as f:
        json.dump(saved_data, f, indent=4)

#############################
## READING THE STORAGE
#############################
# if only key is supplied, we read the keys from a file and print out values corresponding to the key
if args.key and not args.val:
    
    #if file doesn't exist - error
    if not os.path.exists(storage_path):
        print(None)
    #else reading data from storage
    else:
        with open(storage_path, 'r') as f:
            saved_data = json.load(f)
        
        #if key is in the storage, then print value
        if args.key in saved_data.keys():
            print(saved_data[args.key])
        #if not, print None
        else:
            print(None)
