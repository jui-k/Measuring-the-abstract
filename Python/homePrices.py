import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    
    if(len(line)>4):
        area=line[0]
        if('"' in area):
            area= area.replace('"', '')

        if(line[-4]!='-'and line[-4]!='Price'):
            pin=line[-4].split("-")
            high=int(pin[0])
            low=int(pin[-1])
            avg=(high+low)/2
            value=area+"\t"+str(avg)
            print(value)
            
            with open("homePrices_EditedAvg.txt","a") as file:
                file.write(value+"\n")
'''
    with open("homePrices.txt","a") as file:
         file.write(value+"\n")

'''
        
