import statistics as s
import numpy as np
dic1={}
dic2={}
lis1=[]
lis2=[]
lis3=[]

def homes():
    with open('homePrices_EditedAvg.txt') as f:
        line = f.readlines()
        for i in range (1,len(line)):
            area=line[i]
            area=area.split('\t')
            print(area)

    
        

homes()


for i in range (1,len(lis2)):
    if(lis2[i] in lis1):
        print(lis2[i])

