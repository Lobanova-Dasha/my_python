#! python3
# functionals.py

# Map and Lambda Function
cube = lambda x: x*x*x 

def fibonacci(n):
    fib = []
    a, b = 0, 1
    for i in range(0, n):
        fib.append(a)
        a, b = b, a + b
    return fib    
  

print(list(map(cube, fibonacci(int(input()))))) 