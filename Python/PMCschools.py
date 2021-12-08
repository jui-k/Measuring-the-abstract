import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")

    if(len(line)>4):
        school=line[2]
        if('"' in school):
            school= school.replace('"', '')

        area=line[3]
        if('"' in area):
            area= area.replace('"', '')
        value=school+"\t"+area
        print(value)

        with open("PMCschools.txt","a") as file:
             file.write(value+"\n")
                
    
 

