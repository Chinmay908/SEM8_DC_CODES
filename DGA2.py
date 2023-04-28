import numpy as np
from datetime import timedelta

ag_t = input("Enter agreed upon time in HH:MM : ")
n = int(input("Enter the no. of machines : "))
ct_t = [x for x in input("Enter current time of machines in HH:MM : ").split()]


def calc_t(time):
    a, b = time.split(':')
    sec = int(a)*60*60 + int(b)*60
    return(sec)

calc_ag_t = calc_t(ag_t)
calc_ct_t = []

for t in ct_t:
    calc_ct_t.append(calc_t(t))

skews = [] 
for i in range(n):
    print('Current time: ', end='\t')

    skew = []

    for j in range(n):
        print(timedelta(seconds = calc_ct_t[j]), end="\t")
        skew.append(round((calc_ct_t[j] - calc_ag_t)/60))
    
    for j in range(n):
        if(calc_ct_t[j] == calc_ag_t):
            print("\nMessage sent by Machine {}".format(j+1))
    skews.append(skew)


    print('Skew: ', end='\t')
    for j in range(n):
        print(skew[j], end='\t')
        if i < n-1:
            calc_ct_t[j] += 5*60  
    print('\n')

print("\n")
skews = np.array(skews)
avg_skews = np.array(np.sum(skews, axis = 0)/n)
print("Average of skews : ", avg_skews)
print("\n")

for i in range(n):
    if avg_skews[i] > 0:
        print("Machine {} is ahead by {}.".format(i+1, abs(avg_skews[i])))
        print("Therefore decrease its clock by {} to get {}\n".format(abs(avg_skews[i]), 
                        timedelta(seconds = calc_ct_t[i]) - timedelta(minutes = abs(avg_skews[i]))))
    else:
        print("Machine {} is behind by {}.".format(i+1, abs(avg_skews[i])))
        print("Therefore increase its clock by {} to get {}\n".format(abs(avg_skews[i]), 
                        timedelta(seconds = calc_ct_t[i]) + timedelta(minutes = abs(avg_skews[i]))))
