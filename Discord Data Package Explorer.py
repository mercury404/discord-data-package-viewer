# My code sucks, its just a little side project i tried to get on with.
# Imports
import json
#load = input("Enter the path of your user.json here: ")
load = "C:\\Users\\barte\\Downloads\\package\\account\\user.json"
while True:
    try:
        # Loading the json and checking the file path
        with open(load) as f:
            data = json.load(f)
            print("Valid")
            break
    except:
        print("Invalid")
        load = input("Enter the path of your user.json here: ")
# Grabbing data from the json
id = data['id']
username = data['username']
discriminator = data['discriminator']
verified = data['verified']
mobile = data['has_mobile']
status = data['settings']['settings']['status']['status']
# Checks if your status is dnd and turns the status variable into dnd
if status == "dnd":
    status = "Do not disturb"
# Grabbing data from json 2
cstatus = data['settings']['settings']['status']['customStatus']['text']
showgame = data['settings']['settings']['status']['showCurrentGame']
theme = data['settings']['settings']['appearance']['theme']
devmode = data['settings']['settings']['appearance']['developerMode']
version = data['settings']['settings']['versions']['clientVersion']
locale = data['settings']['settings']['localization']['locale']
# Prints all of the fancy stuff
print("-------------- MAIN --------------")
print("ID: "+id)
print("Username: "+username+"#"+str(discriminator))
print("Verified: "+str(verified))
print("Mobile User: "+str(mobile))
print("------------ SETTINGS ------------")
print("Status: "+status)
print("Custom Status: "+cstatus)
print("Theme: "+theme)
print("Developer Mode: "+str(devmode))
print("Client Version: "+str(version))
print("Show Current Game: "+str(showgame))
print("Locale: "+locale)
