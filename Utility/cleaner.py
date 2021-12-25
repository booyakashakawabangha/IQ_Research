# Python programme which deletes all unnecessary columns.

content = []
with open("VIQT_data.csv") as file:
    dirty = file.readlines()
    for line in dirty:
        line = line.split("\t")
        cleaned = line[92:94] + line[97:98] + line[100:101] + \
            line[121:123] + line[126:127] + line[-1:]
        content.append(cleaned)


with open("cleaned.csv", "w") as writer:
    for line in content:
        string = "\t".join(line)
        writer.write(string)

