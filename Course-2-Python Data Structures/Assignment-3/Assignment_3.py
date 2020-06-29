#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
list = []
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        line= line.strip('X-DSPAM-Confidence:')
        line= line.lstrip()
        Float_value = float(line)
        list.append(Float_value)
        continue
Total = 0
Total = float(Total)
for i in range(0,len(list)):
    Total = Total + list[i]

Average = Total / len(list)
print("Average spam confidence:",Average,)

