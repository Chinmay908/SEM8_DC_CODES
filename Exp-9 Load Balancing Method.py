n_servers = int(input("Enter no. of servers: "))
n_processes = int(input("Enter no. of processes: "))

def rrlb(n_servers,n_processes):
    lst = []
    for i in range(n_processes):
        lst.append((i%n_servers)+1)

    print()

    for i in range(n_servers):
        print("Server {} has {} processes".format(i+1,lst.count(i+1)))


while True:
    rrlb(n_servers, n_processes)
    choice = int(input("\n1.Add Server\n2.Remove Server\n3.Add Process\n4.Remove Process\n5.Exit\n\nEnter your choice: "))

    if choice == 1:
        n_servers += 1
    elif choice == 2:
        n_servers -= 1
    elif choice == 3:
        n_processes += 1
    elif choice == 4:
        n_processes -= 1
    else:
        break

