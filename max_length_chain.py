
P = [ [5, 24], [39, 60],[15, 28], [27, 40], [50, 90] ]

print(P[0][0+1])

Q =[]

for i in range(0,len(P)-1):


    if P[i][1] < P[i+1][0]:
        Q.append(P[i])    

    else:
        pass
Q.append(P[-1])
print(len(Q))

