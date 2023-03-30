import gzip

# open file and get all zips from NYSvoters
with gzip.open("NYSvoters", "rt") as l:
        for line in l:
            new = line.split("\t")
            try: zip = int(new[11])
            except: zip = 0
            print(zip)
