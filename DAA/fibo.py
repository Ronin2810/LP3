def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_numbers = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")
