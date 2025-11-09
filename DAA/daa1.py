## ---------- Non Recursive ------------ ##

def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


n = int(input("Enter n: "))
print(f"Fibonacci({n}) = {fib_iterative(n)}")


## ---------- Recursive ------------ ##

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

n = int(input("Enter n: "))
print(f"Fibonacci({n}) = {fib_recursive(n)}")


## ---------- TOH ------------ ##

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Step 1: Move n-1 disks from source → auxiliary
    tower_of_hanoi(n - 1, source, target, auxiliary)
    # Step 2: Move remaining disk from source → target
    print(f"Move disk {n} from {source} to {target}")
    # Step 3: Move n-1 disks from auxiliary → target
    tower_of_hanoi(n - 1, auxiliary, source, target)

n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')
