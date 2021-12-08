import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    pin=line[-5][-6:]
    bank=line[0]
    if(bank[0]=='"'):
        bank = bank.replace('"', '') 
    print(bank+"\t"+pin)
 
    with open("banks.txt","a") as file:
        file.write(bank+"\t"+pin+"\n") 
