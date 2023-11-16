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

def get_fibonacci_input():
    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to generate: "))
            if n < 0:
                print("Please enter a non-negative integer. Try again.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter an integer. Try again.")

if __name__ == "__main__":
    n = get_fibonacci_input()
    fibonacci_numbers = fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")