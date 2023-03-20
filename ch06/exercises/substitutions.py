import json

# data = open("subs.json", "r").read()
# # substitutions = json.loads(data)
# print(substitutions, type(substitutions))

def main():
    file_pointer = open("news.txt", "r")
    file_txt = file_pointer.read()

    file_pointer.close()
    fptr = open("subs.json", "r")
    data = json.load(fptr)
    for k, v, in data.items():
        file_txt = file_txt.replace(k, v)
        print(k, v)
    
    filenew = open("better_news.txt", "w")
    filenew.write(file_txt)
    filenew.close()


main()
