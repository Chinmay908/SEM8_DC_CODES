from datetime import timedelta
from tabulate import tabulate
num = {'00':0,'01':1,'02':2,'03':3,'04':4,'05':5,'06':6,'07':7,'08':8,'09':9}

curr_time = {}
skewdct = {}

machines = ['Machine']
curr_time_lst = ['Current Time']
skew_lst = ['Skew']

def calTime(time):
    a,b = time.split(':')
    if b in num:
        b = num[b]
    secs = int(a)*60*60 + int(b)*60
    td = timedelta(seconds=secs)
    return td

def calcSkew():
    for t in curr_time:
        diff = curr_time[t] - ag_time
        diff_in_min = int(diff.total_seconds()/60)
        skewdct[t].append(diff_in_min)
        skew_lst.append(diff_in_min)

        if ag_time == curr_time[t]:
            print("\nMessage sent by Machine {}".format(t))

def calcSync(avg,m):

    abs_avg = abs(avg)
    print('Current Time of Machine {}: {}'.format(m,curr_time[m]))

    if avg > 0:
        new_time = curr_time[m] - timedelta(minutes=abs_avg)
        print('Hence decreases its clock by {} to get time:{} '.format(abs_avg, str(new_time)))
    else:
        new_time = curr_time[m] + timedelta(minutes=abs_avg)
        print('Hence increases its clock by {} to get time:{} '.format(abs_avg, str(new_time)))

ag_time = input("Enter Agreed Upon Time: ")
n = int(input("Enter no. of machines: "))
time_lst = [x for x in input("Enter current time of {} Machines: ".format(n)).split()]

ag_time = calTime(ag_time)

for i in range(0,n):
    curr_time[i+1] = calTime(time_lst[i])
    curr_time_lst.append(curr_time[i+1])
    skewdct[i+1] = []
    machines.append(i+1)

print('\nAgreed Upon Time: ',str(ag_time))
calcSkew()
print(tabulate([machines,curr_time_lst,skew_lst],tablefmt="grid"))

counter = 1

while counter != n:
    print("\nAfter 5 mins:")
    curr_time_lst = ['Current Time']
    skew_lst = ['Skew']

    for t in curr_time:
        curr_time[t] += timedelta(minutes=5)
        curr_time_lst.append(curr_time[t])

    calcSkew()
    print(tabulate([machines,curr_time_lst,skew_lst],tablefmt="grid"))

    counter+=1

for i in skewdct:
    s=0
    for skew in skewdct[i]:
        s += skew
    avg = s/n
    print("\nSkew of Machine {} is {}".format(i,avg))
    calcSync(avg,i)