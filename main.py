pathtofile = "data.csv"

with open(pathtofile, 'r') as filereader:

    line = filereader.readline()

    while line:
        #print(line.strip())
        items = line.strip(',')
        print(items)
        line = filereader.readline()
