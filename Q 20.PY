Q.20) Prime finder: Loop 1-100, check primality with while/for, store in set, list primes in dict 
by digit sum.



# Program to find prime numbers from 1 to 100
# and group them by the sum of their digits

# Set to store prime numbers
primes = set()

# Check numbers from 1 to 100
for num in range(2, 101):
    is_prime = True   # assume number is prime

    # Check if number is divisible by any smaller number
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # If still prime, add to set
    if is_prime:
        primes.add(num)

print("Prime numbers from 1 to 100:")
print(primes)

# Dictionary to group primes by digit sum
prime_dict = {}

# Loop through each prime number
for p in primes:
    # Find sum of digits (example: 23 → 2 + 3 = 5)
    digit_sum = 0
    for d in str(p):
        digit_sum = digit_sum + int(d)

    # Store prime in dictionary using digit_sum as key
    if digit_sum in prime_dict:
        prime_dict[digit_sum].append(p)
    else:
        prime_dict[digit_sum] = [p]

print("\nPrime numbers grouped by digit sum:")
for key, value in prime_dict.items():
    print("Digit sum", key, ":", value)




OUTPUT: 
Prime numbers from 1 to 100:
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

Prime numbers grouped by digit sum:
Digit sum 2 : [2]
Digit sum 3 : [3]
Digit sum 5 : [5, 23, 41]
Digit sum 7 : [7, 43, 61]
Digit sum 11 : [11, 29, 47]
Digit sum 13 : [13, 31]
Digit sum 17 : [17, 53, 71]
Digit sum 19 : [19, 73]
Digit sum 14 : [59]
Digit sum 16 : [67]
Digit sum 20 : [83]
Digit sum 17 : [89]
Digit sum 16 : [97]
