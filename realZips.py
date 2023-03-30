# open NY zips and zips in data file
with open("properNYzips") as f:
    proper = f.read()

with open("uniqZips") as a:
    unique = a.read()

p = proper.split("\n")
u = unique.split("\n")

# check if zip from file is a real NY zip code
for i in u:
    if i in p:
        print(i)
