import gzip

# open files
with open("realZips.txt") as n:
    NYzips = n.read()

with open("cNames.txt") as c:
    cNames = c.read()

with open("pocNames.txt") as p:
    pocNames = p.read()


zips = NYzips.split("\n")

# create dictionaries to hold data
cPurge = {}
pPurge = {}
popC = {}
popP = {}
totalVoters = {}

# set dictionaries to 0 initially for every zip code
for z in zips:
    cPurge[str(z)] = 0
    pPurge[str(z)] = 0
    popC[str(z)] = 0
    popP[str(z)] = 0
    totalVoters[str(z)] = 0

# open NYS data
with gzip.open("NYSvoters", "rt") as a:
    for l in a:
        line = l.split("\t")
        try: zip = int(line[11])
        except: zip = 0

        # check if the zip is used
        if str(zip) in zips:
            zip = str(zip)
            totalVoters[zip] += 1

            # check if the name is caucasian
            if line[0] in cNames:
                popC[zip] += 1

                # check if purged
                if line[39] == "PURGED":
                    cPurge[zip] += 1

            # check if name is poc
            elif line[0] in pocNames:
                popP[zip] += 1

                # check if name is purged
                if line[39] == "PURGED":
                    pPurge[zip] += 1 

# print the data as long as there were more than 100 votes in the zip code
for i in totalVoters:
    if int(totalVoters[i]) > 100:
        print(int(i), "|", int(cPurge[i]), "|", int(popC[i]), "|", int(pPurge[i]), "|", int(popP[i]), "|", int(totalVoters[i]), "|")


         
 

               
