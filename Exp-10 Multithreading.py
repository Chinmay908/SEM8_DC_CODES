import threading

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Create thread functions to generate prime numbers and Fibonacci sequence
def generate_primes(num):
    for i in range(2, num+1):
        if is_prime(i):
            print(f"Prime: {i}", end="\n")

def generate_fibonacci(num):
    # fib = fibonacci(num)
    a = 0
    b = 1
    if num >= 1:
        print("Fibo 1: ", a, end="\n")
    if num >= 2:
        print("Fibo 2: ", b, end="\n")
    if num >= 3:
        for i in range(2, num):
            c = a + b
            print("Fibo {}: ".format(i+1), c, end="\n")
            a = b
            b = c

# Create and start threads to generate prime numbers and Fibonacci sequence
prime_thread = threading.Thread(target=generate_primes, args=(20,))
fibonacci_thread = threading.Thread(target=generate_fibonacci, args=(10,))
prime_thread.start()
fibonacci_thread.start()

# Wait for the threads to finish
prime_thread.join()
fibonacci_thread.join()