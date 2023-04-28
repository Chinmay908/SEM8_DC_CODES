n = int(input("Enter the no. of machines : "))
p_ind = int(input("Enter index of machine P which sends the message : "))
failed_ind = int(input("Enter the index of failed coordinator : "))

for i in range(p_ind, n-1): #last cannot send message to any machine
  if i != failed_ind:
    print("{} sends an election message to machine ---> ".format(i), end="")
    for j in range(i+1, n):
      print(j, end="  ")
    
    li = []
    for j in range(i+1, n):
      if j != failed_ind:
        new_coordinator = j
        li.append(j)

    if len(li) != 0:
      print("\nOK message sent by machine ---> ", end="")
      for item in li:
        print(item, end=" ")
    print("\n\n")

print("New coordinator : ", new_coordinator)
print("\n{} sends coordinator message to machine ---> ".format(new_coordinator), end="")
for i in range(0, new_coordinator):
  if i != failed_ind:
    print(i, end="  ")
