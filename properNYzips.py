
# create list for zips
i = []

# open file
with open("NYzips") as f:
    # loop through lines and add 4th field to i
    for l in f:
        line = l.split(",")
        try: zip = int(line[4].strip())
        except: zip = 0
        i.append(zip)

# return list of zips
print(i)
