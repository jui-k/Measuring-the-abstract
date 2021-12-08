import statistics as s
import numpy as np

def hotels():
    lis=[]
    dic1={}
    with open('hotel.txt') as f:
        line = f.readlines()
        for i in range (1,len(line)):
            pin=line[i][-7:-1]
            if pin not in dic1:
                dic1[pin]=1;
            else:
                dic1[pin]+=1;

    dic2={}
    dic2=dict(sorted(dic1.items(),key= lambda x:x[1]))

    for key in dic2:
        print(key, dic2[key])
        lis.append(dic2[key])
        
    print(lis)
    quartiles = s.quantiles(lis, n=2)
    print("Quartiles are: " + str(quartiles))
    #print(np.percentile(lis, 75))

hotels()
