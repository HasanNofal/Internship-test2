import sys
import json
f = open(".\countries.json", "r")
data = f.read()
countries_list = json.loads(data)
f.close()
num_of_parameters = len(sys.argv) - 1
if num_of_parameters == 0:
    print("The parameter is missing from the cli")
elif num_of_parameters == 1:
    translation_key = sys.argv[1]
    for country in countries_list:
        try:
            print(country["translations"][translation_key]["official"])
        except:
            print("The translation key does not exist")
else:
    print("Please enter one translation key only")