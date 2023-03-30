# open file
with open("lastNamesOut.txt") as f:
    # loop through lines and check if he last name is usually caucasian of poc
    for l in f:
        line = l.split("|")
        if line[4] > line[3] or line[5] > line[3] or line[6] > line[3] or line[7] > line[3] or line[8] > line[3]:
            poc = open("pocNames", "a")
            poc.write(line[1] + "\n")

        else:
            c = open("cNames", "a")
            c.write(line[1] + "\n")
        
