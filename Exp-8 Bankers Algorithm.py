p = int(input("Enter the no. of processes: "))
r = int(input("Enter the no. of resources: "))

instances = []
print()
for i in range(r):
  instance = int(input("Enter the instances of resource type R{}: ".format(i+1)))
  instances.append(instance)

max = []
print("\nEnter the Max matrix for each process:")
for i in range(p):
  max_i = [int(item) for item in input("P{}: ".format(i+1)).split()]
  max.append(max_i)

alloc = []
print("\nEnter the Allocated matrix for each process:")
for i in range(p):
  alloc_i = [int(item) for item in input("P{}: ".format(i+1)).split()]
  alloc.append(alloc_i)

completed = []
for i in range(p):
    completed.append(0)

sum = []
for i in range(r):
    sum.append(0)

for i in range(p):
    for j in range(r):
        sum[j] += alloc[i][j]

avail = []
for i in range(r):
    avail.append(instances[i] - sum[i])

need = []
print("\nNeed matrix: ")
for i in range(p):
    need_i = []
    print("P{}: ".format(i + 1), end="")
    for j in range(r):
        print(max[i][j] - alloc[i][j], end=" ")
        need_i.append(max[i][j] - alloc[i][j])
    print()
    need.append(need_i)

count = 0
safeSequence = []
start = 0

while True:
    process = -1
    for i in range(start, p):
        if completed[i] == 0:
            process = i
            for j in range(r):
                if (avail[j] < need[i][j]):
                    process = -1
                    break

        if process != -1:
            break

    if process != -1:
        safeSequence.append(process + 1)
        count += 1
        for j in range(r):
            avail[j] += alloc[process][j]
            alloc[process][j] = 0
            max[process][j] = 0
            completed[process] = 1

    if count != p and process != -1:
        if (process + 1 == p):
            start = 0
        else:
            start = process + 1
        continue
    else:
        break

if (count == p):
    print("\nThe system is in a Safe State.")
    print("Safe Sequence : < ", end="")
    for i in range(p):
        print("P{}".format(safeSequence[i]), end=" ")
    print(">")
else:
    print("\nThe system is in an Unsafe State.")