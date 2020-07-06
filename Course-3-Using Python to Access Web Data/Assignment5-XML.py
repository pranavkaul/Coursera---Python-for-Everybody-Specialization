'''In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_690528.xml (Sum ends with 14)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.'''


from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('Retrieving:',url)
html = urlopen(url, context=ctx).read()

stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
final = []
count = 0
for item in lst:
    count += 1
    sum_count = item.find('count').text
    sum1 = int(sum_count)
    final.append(sum1)

print(count)
print(sum(final))


