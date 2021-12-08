'''
import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    addr = line[2].split("-")
    
    pin=addr[-1]
    
    location=line[1]
    print(location+"\t"+pin)

    with open("pin.txt","a") as file:
        file.write(location+"\t"+pin+"\n")
'''


import sys

for line in sys.stdin:
    line=line.strip()
    add=line.split(",")
    line=line.split("-")
    pin=line[-1]
    
    if('"' in pin):
        pin = pin.replace('"','') 
    if(len(add)>2 and len(pin)<8):
       add = add[1]
       value = pin+"\t"+add
       print(value)

       with open("pin.txt","a") as file:
            file.write(value+"\n")
