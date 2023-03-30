# names 1-1000

import re

pat = re.compile(
    r'<tr>.*?<td>([^<]+)</td>.*?<td>.*?<a.*?>([^<]+).*?<td>([^<]+).*?<td>([^<]+).*?<td>([^<]+).*?<td>([^<]+).*?<td>([^<]+).*?<td>([^<]+).*?<td>([^<]+)',
    flags=re.DOTALL
)


# read the entire page and turn it into a string
data1 = open("lastNames1000.html").read()
data2 = open("lastNames2000.html").read()
data3 = open("lastNames3000.html").read()
data4 = open("lastNames4000.html").read()
data5 = open("lastNames5000.html").read()

if data1:
    table = re.findall(pat, data1)
    table += re.findall(pat,data2)
    table += re.findall(pat,data3)
    table += re.findall(pat, data4)
    table += re.findall(pat, data5)

    
    for row in table:
        print(row[0] + "|" + row[1] + "|" + row[2] + "|" + row[3] + "|" + row[4] + "|" + row[5] + "|" + row[6] + "|" + row[7] + "|" + row[8])
