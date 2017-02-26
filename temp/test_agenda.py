w = open("asian.txt", 'w')

with open("ref/DD_asian.txt", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip().split("\t")[0]
        w.write(line + "\n")