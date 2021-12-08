import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    pin=line[-4][-7:-1]
    hotel=line[0]
    if(hotel[0]=='"'):
        hotel = hotel.replace('"', '')
    print(hotel+"\t"+pin)

    with open("hotel.txt","a") as file:
        file.write(hotel+"\t"+pin+"\n") 



