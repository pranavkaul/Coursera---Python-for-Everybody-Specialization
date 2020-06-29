#Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
fname = input("Enter file name: ")
fhandle = open(fname)
for i in fhandle:
    i = i.rstrip()
    i_final = i.upper()
    print(i_final)

