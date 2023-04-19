import json
import random

def main():
    json_data = json.load(open("file.txt", "r"))
    print(random.choice(json_data))


main()