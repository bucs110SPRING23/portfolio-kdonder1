import json

def main():
    file_pointer = open("news.txt", "r")
    fptr = open("subs.json", "r")
    file_txt = file_pointer.read()
    data = json.load(fptr)

    file_pointer.close()
    
    for k, v, in data.items():
        file_txt = file_txt.replace(k, v)
        print(k, v)
    
    filenew = open("better_news.txt", "w")
    filenew.write(file_txt)
    filenew.close()


main()
