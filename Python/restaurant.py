import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    restaurant = line[0]
    pin = line [-1][-7:-1]
    print(restaurant + "\t" + pin)

    with open("restaurant.txt","a") as file:
        file.write(restaurant + "\t" + pin + "\n")
    
    
