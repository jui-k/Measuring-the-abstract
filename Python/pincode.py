import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    pin=line[1]
    location=line[0]
    print(location+"\t"+pin)

    with open("pin.txt","a") as file:
        file.write(location+"\t"+pin+"\n")

