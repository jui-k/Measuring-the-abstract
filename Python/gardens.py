import sys

dict={}
value=""
for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=line[0].split(",")
    area=line[-1]
    if(len(area)>0):
        #print(area)
        if(area not in dict):
            dict[area]=1
        else:
            dict[area]+=1
for key in dict:
    value=key+"\t"+str(dict[key])
    print(value)
    with open("garden.txt","a") as file:
            file.write("\n"+value) 

