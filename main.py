import sys, json
f = open(".\countries.json", "r")
data = f.read()
countries_list = json.loads(data)
try:
    translation_key = sys.argv[1]
    for country in countries_list:
        try:
            print(country["translations"][translation_key]["official"])
        except:
            print("The translation key does not exist")
except:
    print("The parameter is missing from the cli")