#  Medium
num_primes = int(input("How many primes u want? "))  # Input Number
primes = []  # List to store prime numbers
num = 2  # Start checking from the first prime number, which is 2

# Continue the loop until we find the required number of prime numbers
while len(primes) < num_primes:
    is_prime = True  # Assume the current number is prime initially

    # Check if the current number is divisible by any previously found prime
    for prime in primes:
        if prime * prime > num:  # No need to check beyond the square root of num
            break
        if num % prime == 0:  # If divisible, it's not a prime
            is_prime = False
            break

    if is_prime:
        primes.append(num)  # If still prime, add it to the list of prime numbers

    num += 1  # Move to the next number to check

print(primes)