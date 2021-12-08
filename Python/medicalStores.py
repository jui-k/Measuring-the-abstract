import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    
    if(len(line)>4):
        store=line[0]
        if('"' in store):
            store= store.replace('"', '')
        
        pin=line[-4][-7:-1]
        value=pin+"\t"+store
        print(value)

    with open("medicalStore.txt","a") as file:
            file.write(value+"\n")
                
   
