from datetime import timedelta

nc = int(input("Enter no. of clients "))
tc = [x for x in input("Enter time of clients in HH:MM : ").split()]
ts = input("Enter the time of server ")

def calc_t(time):
    a, b = time.split(':')
    sec = int(a)*60*60 + int(b)*60
    return(sec)

cal_ts = calc_t(ts)
cal_tc = []

for t in tc:
  cal_tc.append(calc_t(t))

sum=0
for i in cal_tc:
  sum+=i

sum+=cal_ts
avg_t = int(sum/(nc+1))
# print(avg_t)
# sync_t = timedelta(seconds=avg)

if cal_ts == avg_t:
  print("Server is already synchronized")
elif cal_ts < avg_t:
  item = timedelta(seconds = avg_t - cal_ts)
  print("Server is behind ,increase its clock by {},so now its time is {} ".format(item,timedelta(seconds = avg_t)))
elif cal_ts > avg_t:
  item = timedelta(seconds = cal_ts - avg_t)
  print("Server is ahead ,decrease its clock by {},so now its time is {} ".format(item,timedelta(seconds = avg_t)))

print()

for i in range(nc):
  if cal_tc[i]>avg_t:
        print("Client {} is ahead by {}.".format(i, timedelta(seconds = abs(avg_t - cal_tc[i]))))
        print("Therefore decrease its clock to get {}\n".format(timedelta(seconds = avg_t)))
                       
  elif cal_tc[i]==avg_t:
        print("Client {} is already synchronized to time {}".format(timedelta(seconds = avg_t)))
  else:
        print("Client {} is behind by {}.".format(i, timedelta(seconds = abs(avg_t - cal_tc[i]))))
        print("Therefore increase its clock to get {}\n".format(timedelta(seconds = avg_t)))
