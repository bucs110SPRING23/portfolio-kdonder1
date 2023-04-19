import json

# json is a string format, not a file format

# files
# - saved program state

# Operating System: manage files
# request the file from OS
# - where
# - name
# - how to use it

# - working with files is one-way

def main():
    file_pointer = open("ideas.txt", "r") # FILE
    # ideas = file_pointer.readlines()
    # print(ideas[1])

    # # idea = input("Enter an idea: ")
    # # ideas = []
    # # ideas.append(idea)

    # ideas = file_pointer.readline()
    # print(ideas)
    # ideas = file_pointer.readline()
    # print(ideas)

    file_pointer = open("assets/ideas.txt", "a") # the file gets truncated
    
    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)

# character for a line break is \n
    for i in ideas:
        file_pointer.write(i + "\n")
        x = 5/0
    file_pointer.close()

    # LOOK IN NOTES

    open("assets/ideas.text", "r").read() # truncate the file
    data = json.loads(file_contents)
    print(data, type(data))
# in json, everything is automatically converted to the type it needs to be in



main()