#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
filehandle = open(name)
counts = dict()
for line in filehandle:
    if not line.startswith('From '):
        continue
    words = line.split()
    words_final = words[5].split(':')
    words_final_1 = words_final[0]
    counts[words_final_1] = counts.get(words_final_1, 0) + 1

list = []
for key, value in counts.items():
    list.append((key, value))

list.sort()
for key,value in list:
    print(key, value)