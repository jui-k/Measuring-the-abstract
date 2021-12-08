import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    line = str(line[0]).split(",")
    pin = line[-4][-7:-1]
    station = line[0]
    print(station+"\t"+pin)

    with open("pin.txt","a") as file:
        file.write(station + "\t" + pin + "\n")

    
