import os

with open("file.txt", "r") as in_file:
    buf = in_file.readlines()

text_to_search = 'public const string AssemblyGearIcon'
text_to_insert = 'this is new line added'

with open("file.txt", "w") as out_file:
    for line in buf:
        if (line.find(text_to_search) != -1) :
        #if line == "; Include this text\n":
            line = text_to_insert + "\n" + line
        out_file.write(line)