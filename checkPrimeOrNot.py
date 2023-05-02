# which number has a only two factors 1 and itself, then that is the prime number.
# Natural number ->> 1
# Which has only two factors 1 and itself.

# 19 => 1 and 19 ->> prime number
# 28 => 1,2,4,7,14,28 ->> not a prime number

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter the number which you want to check: "))
if is_prime(n):
    print(f"Given number {n} is prime.")
else:
    print(f"Given Number {n} is not prime.")