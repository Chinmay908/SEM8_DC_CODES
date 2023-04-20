no_of_machines = int(input("Enter no. of machines: "))
detect_machine = int(input("Enter machine who sends a message: "))
down_machine = int(
    input("Enter machine who does not respond to Machine {} within time interval T: ".format(detect_machine)))

high_priority_machines = []

for i in range(detect_machine + 1, no_of_machines + 1):
    if (i != down_machine):
        high_priority_machines.append(i)

print()

print("Machine {} sending Election Message to Machines ---->".format(detect_machine), end=" ")
for i in high_priority_machines:
    print(i, end=" ")

print("\n")

repsonse_high_priority_machines = {}

l = len(high_priority_machines)
c = 0
for i in range(0, l):
    c += 1
    print("Machine {} responding OK to the Election Message".format(high_priority_machines[i]))

print("\nNo of machines responded OK to Election Message:", c)

while (len(high_priority_machines) != 1):
    c = 0
    sender = high_priority_machines[0]
    l = len(high_priority_machines)
    print("\nMachine {} sending Election Message to Machines ---->".format(sender), end=" ")
    for i in range(1, l):
        print(high_priority_machines[i], end=" ")

    print("\n")

    for i in range(1, l):
        c += 1
        print("Machine {} responding OK to the Election Message".format(high_priority_machines[i]))

    print("\nNo of machines responded OK to Election Message:", c)
    high_priority_machines.pop(0)

print("\nMachine {} elected as the New Coordinator\n".format(high_priority_machines[0]))

print("Machine {} sending message I am the New Coordinator to Machines ---->".format(high_priority_machines[0]),
      end=" ")

for i in range(1, no_of_machines):
    if (i == down_machine or i == high_priority_machines[0]):
        continue
    print(i, end=" ")