import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    
    if(len(line)>4):
        museum=line[0]
        if('"' in museum):
            museum= museum.replace('"', '')
        
        pin=line[-4][-7:-1]
        value=museum+"\t"+pin
        print(value)

    with open("museum.txt","a") as file:
         file.write(value+"\n")
                
   
