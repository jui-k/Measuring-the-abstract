import sys

npin=""
for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=line[0].split(",")
    
    
    if(len(line)>4):
        #pin value
        pin=line[-3].split("-")
        pin=pin[-1]
        if(' ' in pin):
            pin= pin.replace(' ', '')
            if('"' in pin):
                pin= pin.replace('"', '')
                if('.' in pin):
                    pin= pin.replace('.', '')
                    if(len(pin)==6):
                        npin= pin
        
        #place value
        place=line[1]
        if(place[0]=='"'):
            place= place.replace('"', '')
        value=place+"\t"+npin
        print(value)

        with open("place.txt","a") as file:
            file.write(value+"\n") 

