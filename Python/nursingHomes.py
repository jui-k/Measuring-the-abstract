import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    
    
    if(len(line)>4):
        hospital=line[2]
        if('"' in hospital):
            hospital= hospital.replace('"', '')
            
        pin=line[-5][-3:-1]
        if('-' in pin):
                pin= pin.replace('-', '')
        elif('.' in pin):
                pin= pin.replace('.', '')
        elif(' ' in pin):
                pin= pin.replace(' ', '')
        elif(pin.isalpha()==False):
            if(len(pin)==1):
                pin= "41100"+pin
            elif(len(pin)==2):
                pin= "4110"+pin
            value=pin+"\t"+hospital
            print(value)

            with open("nursing.txt","a") as file:
                file.write(value+"\n") 



