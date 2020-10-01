#importing requests library
import requests

#grabbing data from freegeoip json api
#using method get to grab data from site
#using method json to read data into internal python representation
def get_location_info():
    return requests.get("https://freegeoip.app/json/").json()

#checking that the program is started with python interpreter
if __name__ ==  "__main__":
    print(get_location_info())