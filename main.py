import sys
import json

# Convert json file to list
f = open("./countries.json", "r")
data = f.read()
countries_list = json.loads(data)
f.close()

# Check if number of input parameters is correct
num_of_parameters = len(sys.argv) - 1
if num_of_parameters == 0:
    print("The parameter is missing from the cli")

elif num_of_parameters == 1:
    translation_key = sys.argv[1]
    key_exist = False

    # check if key exist for atleast one country
    for country in countries_list:
        if translation_key in country["translations"]:
            key_exist = True
            break

    # Exit the program if translation doesnt exist for all countries
    if key_exist == False:
        print("Translation key doesn't exist for all countries")
        quit()

    #  print translations if exist
    for country in countries_list:
        try:
            print(country["translations"][translation_key]["official"])
        except:
            print(translation_key + " translation for (" + country["name"]["official"] + ") does not exist")

else:
    print("Please enter one translation key only")
