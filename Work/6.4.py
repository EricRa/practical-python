def filematch(filename, substr):
    with open(filename, "r") as f:
        for line in f:
            if substr in line:
                yield line
                
for line in filematch("Data/portfolio.csv", "IBM"):
    print(line, end="")