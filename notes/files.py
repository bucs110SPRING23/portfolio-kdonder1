import json


def main():
    file_pointer = open("file.txt", "r") # modes: 'r', 'w', 'a'
    file_contents = file_pointer.readlines() # each lines as a string in a list
    file_contents1 = file_pointer.readline() # first line as a string
    file_contents2 = file_pointer.readline() # second line as a string
    file_contents = file_pointer.read() # entire files in a single string
    # for line in file_pointer:
    #   print(line)

    #file streams = one way

    #'w' deletes any existing file, truncate teh file
    file_pointer = open("file.txt", "w")
    file_pointer.write("Hello World") # does not add the newline <enter> like print
    file_pointer.write("\n") # \n
    file_pointer.close() # always close files
    var  = 5/0

main()
