import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    pin=line[-4][-7:-1]
    bus=line[0]
    print(bus+"\t"+pin)
 
    with open("bus.txt","a") as file:
        file.write(bus+"\t"+pin+"\n") 
