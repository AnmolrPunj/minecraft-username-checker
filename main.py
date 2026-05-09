from mojang import API
from mojang.errors import NotFound

api = API()
list_availble = []
with open("usernames.txt") as names:
    for values in names:
        name = values.strip()  

        try:
            api.get_uuid(name)

        except NotFound:
            list_availble.append(name)
        print(f"Checked: {name}")
with open("output.txt", "w") as output:
    for values in list_availble:
        output.write(values + '\n')
    
print('Finished checking usernames! List of availble names produced in output.txt')
