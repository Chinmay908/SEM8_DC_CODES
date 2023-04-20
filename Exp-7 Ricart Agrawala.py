n = int(input("Enter no. of sites: "))

request_set = {}

for i in range(1,n+1):
  lst = []
  for j in range(1,n+1):
    if(i!=j):
      lst.append(j)
  request_set[i] = lst

n = int(input("Enter no. of sites who want to enter the CS: "))

request_sites = []

for i in range(n):
  tupl = [int (x) for x in input("Enter the timestamp and site no. :").split()]
  request_sites.append(tuple(tupl))

print()

request_sites = sorted(request_sites)

# print(request_sites)

for i in request_sites:
  for j in request_set[i[1]]:
    print("Site {} sending request message to site {}".format(i[1],j))

print()

request_site = [] 
 
for i in request_sites:
  request_site.append(i[1])

for tupl in request_sites:

  cur_req_site = tupl[1] #2

  for i in request_set[cur_req_site]: #[1,3]
    if(i not in request_site): #check if the site is not requesting for CS
      print("Site {} sending reply message to site {}".format(i,cur_req_site))

    else: #if it has already requested then check if its timestamp is greater than the requesting site
      for j in request_sites:
        if(i == j[1]):
          if(j[0] > tupl[0]):
            print("Site {} sending reply message to site {}".format(i,cur_req_site))
  
  print("\nSince Site {} has recieved reply messages from all sites in its request set, therfore it enters the CS".format(cur_req_site))

  if(len(request_site)>0):
    print("\nSite {} exits the CS\n".format(cur_req_site))

  request_site.pop(0)
