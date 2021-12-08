import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    line=str(line[0]).split(",")
    pin=line[-4][-7:-1]
    college=line[0]
    if(college[0]=='"'):
        college= college.replace('"', '')
    print(college+"\t"+pin)

    with open("college.txt","a") as file:
        file.write(college+"\t"+pin+"\n") 



