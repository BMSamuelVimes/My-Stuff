# def is_prime(n: int) -> bool:
#     # 1. Handle base cases
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True  # 2 and 3 are prime
    
#     # 2. Eliminate multiples of 2 and 3
#     if n % 2 == 0 or n % 3 == 0:
#         return False
    
#     # 3. Check factors up to √n, skipping multiples of 2 and 3
#     # All primes greater than 3 are of the form 6k ± 1
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
        
#     return True

# # Example usage:
# if __name__ == "__main__":
#     try:
#         user_num = int(input("Enter a number to check: "))
#         if is_prime(user_num):
#             print(f"{user_num} is a prime number!")
#         else:
#             print(f"{user_num} is not a prime number.")
#     except ValueError:
#         print("Please enter a valid integer.")

import math


def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime

    # Exclude multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check factors from 5 up to sqrt(n), skipping even numbers
    # All primes greater than 3 are of the form 6k +/- 1
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def main():
    print("--- Prime Number Checker ---")
    print("Enter a number to check, or type 'End' to quit.\n")

    while True:
        user_input = input("Enter a number: ").strip()

        # Check for exit condition (case-insensitive)
        if user_input.lower() == "end":
            print("Goodbye!")
            break

        # Validate input to ensure it's an integer
        try:
            number = int(user_input)

            if is_prime(number):
                print(f"✨ {number} is a PRIME number.\n")
            else:
                print(f"❌ {number} is NOT a prime number.\n")

        except ValueError:
            print("⚠️ Invalid input. Please enter a valid integer or 'End'.\n")


if __name__ == "__main__":
    main()