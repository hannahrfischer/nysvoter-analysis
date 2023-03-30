import matplotlib.pyplot as plt

# lists for graph
poc = []
c = []

# open file
with open("finalOut") as f:
    for l in f:
        line = l.split("|")
        # make sure denom isn't 0
        if int(line[4]) != 0 and int(line[2]) != 0:
            # append percenage of purged voters
            poc.append((int(line[3])/int(line[4]))*100)
            c.append((int(line[1])/int(line[2]))*100)
             
plt.scatter(c, poc, alpha = .5)
plt.xlabel("Percent of Caucasian Votes Purged")
plt.ylabel("Percent of POC Votes Purged")
plt.title("Is America Racist?")
plt.savefig("graph.pdf")
