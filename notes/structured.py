# protocols
# - http
# - xml
# - json: javascript object notation
#   - string formats, not file formats
#   - int, float, string, bool, list, dictionary, None
#   - {}:dictionary, [] : list

import json

data = {
    "num": 1,
    "msg": "Hello World",
}

json_string = json.dumps(data)
print(json_string, type(json_string))

json_data = json.loads(json_string)

for k, v, in json_data.items():
    print(k, v)

fptr = open("movies.json", "w") # .json is a convention, not a file type
fptr.write(json_string)
fptr.close()

data_str = open("movies.json", "r").read()
data = json.loads(data_str)
print(data, type(data))

data = json.load(open("movies.json", "r"))
print(data, type(data))

fptr = open("movies.json", "w")
data = json.dump(data, fptr)
fptr.close()
print(data, type(data))

def main():
    idea = input("Enter an idea: ")

    file_pointer = open("file.txt", "r")
    data = json.load(file_pointer)
    print(data)
    data.append(idea)
    file_pointer.close()
    # file_pointer = open("assets/data.json", "w")

    file_pointer.write("Hello World") # does not add the newline <enter> like print
    file_pointer.write("\n") # \n
    file_pointer.close() # always close files
