########################### Basic Prime Checking

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


############################## Prime Checking With Factoring
# import math

# def is_prime(n):
#     """Returns True if n is prime, False otherwise."""
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True  # 2 and 3 are prime

#     # Exclude multiples of 2 and 3
#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     # Check factors from 5 up to sqrt(n), skipping even numbers
#     # All primes greater than 3 are of the form 6k +/- 1
#     limit = int(math.isqrt(n))
#     for i in range(5, limit + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False

#     return True

# def get_factors(n):
#     """Return a sorted list of factors of n (including 1 and n)."""
#     if n == 0:
#         return []  # factors for 0 are undefined in this context
#     n_abs = abs(n)
#     factors = set()
#     limit = int(math.isqrt(n_abs))
#     for i in range(1, limit + 1):
#         if n_abs % i == 0:
#             factors.add(i)
#             factors.add(n_abs // i)
#     factors_list = sorted(factors)
#     # Reintroduce sign for negative numbers (optional): show negative factors too
#     if n < 0:
#         neg_factors = [-f for f in reversed(factors_list)]
#         return neg_factors + factors_list
#     return factors_list

# def main():
#     print("--- Prime Number Checker ---")
#     print("Enter a number to check, or type 'End' to quit.\n")

#     history = [] #list of (input_str, number_or_None, result_str, factors_list)

#     while True:
#         user_input = input("Enter a number: ").strip()

#         # Check for exit condition (case-insensitive)
#         if user_input.lower() == "end":
#             print("\n--- Session Summary ---")
#             if not history:
#                 print("No numbers were checked.")
#             else:
#                 for idx, (raw, num, result, factors) in enumerate(history, start=1):
#                     if num is None:
#                         print(f"{idx}. X!Invalid Input!X - {raw}")
#                     else:
#                         if result == "prime":
#                             print(f"{idx}. {num} (P)")
#                         else:
#                             print(f"{idx}. {num} (NP) Factors: {factors}")
#             print("\nGoodbye.")
#             break
       
#         # Validate input to ensure it's an integer
#         try:
#             number = int(user_input)

#             if is_prime(number):
#                 print(f"✨ {number} is a PRIME number.\n")
#                 history.append((user_input, number, "prime", []))
#             else:
#                 factors = get_factors(number)
#                 print(f"❌ {number} is NOT a prime number.\n")
#                 print(f"Factors: {factors}\n")
#                 history.append((user_input, number, "not prime", factors))
#         except ValueError:
#             print("⚠️ Invalid input. Please enter a valid integer or 'End'.\n")
#             history.append((user_input, None, "invalid", []))

# if __name__ == "__main__":
#     main()


#########################Prime Checker with Reporting and Error Checking
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

def get_factors(n):
    """Return a sorted list of factors of n (including 1 and n)."""
    if n == 0:
        return []  # factors for 0 are undefined in this context
    n_abs = abs(n)
    factors = set()
    limit = int(math.isqrt(n_abs))
    for i in range(1, limit + 1):
        if n_abs % i == 0:
            factors.add(i)
            factors.add(n_abs // i)
    factors_list = sorted(factors)
    # Reintroduce sign for negative numbers (optional): show negative factors too
    if n < 0:
        neg_factors = [-f for f in reversed(factors_list)]
        return neg_factors + factors_list
    return factors_list

def parse_input(s: str):
    """Try to parse s as integer. If it's a decimal string (e.g., '3.0') treat as integer only if it has no fractional part.
    Returns (kind, value) where kind in {'int', 'invalid_decimal', 'letters'}.
    - 'int' -> value is int
    - 'invalid_decimal' -> value is original string (we flag as invalid)
    - 'letters' -> value is original string
    """
    s_strip = s.strip()
    if s_strip == "":
        return ("letters", s)
    # Try direct integer
    try:
        return ("int", int(s_strip))
    except ValueError:
        pass
    # Try to detect decimal that is integer-like (e.g., "3.0" -> 3) or non-integer decimal (e.g., "2.5")
    try:
        f = float(s_strip)
    except ValueError:
        return ("letters", s)
    # It's a float; check if it is whole number
    if f.is_integer():
        return ("int", int(f))
    else:
        return ("invalid_decimal", s)

def main():
    print("--- Prime Number Checker ---")
    print("Enter a number to check, or type 'End' to quit.\n")

    history = [] #list of dicts: {'raw':..., 'kind':..., 'value':..., 'result':..., 'factors':...}

    while True:
        user_input = input("Enter a number: ").strip()

        # Check for exit condition (case-insensitive)
        if user_input.lower() == "end":
            print("\n--- Session Summary ---")
            if not history:
                print("No entries were entered.")
            else:
                for i, entry in enumerate(history, start=1):
                    raw = entry['raw']
                    kind = entry['kind']
                    if kind == 'int':
                        num = entry['value']
                        if entry['result'] == 'prime':
                            print(f"{i}. {num}: PRIME")
                        else:
                            factors = entry['factors']
                            if num == 0:
                                print(f"{i}. 0: factor undefined")
                            else:
                                print(f"{i}. {num}: NOT PRIME - Factors: {factors}")
                    elif kind == 'invalid_decimal':
                        print(f"{i}. '{raw}': Invalid (Non-integer Decimal)")
                    else:
                        print(f"{i}. '{raw}': Invalid input")

            print("\nGoodbye.")
            break

        kind, val = parse_input(user_input)
        entry = {'raw': user_input, 'kind': kind, 'value': None, 'fatcors': []}

        if kind == 'int':
            number = val
            entry['value'] = number
            if number == 1:
                print(f"❌ 1 is NOT a prime number.")
                factors = [1]
                print(f"Factors: {factors}\n")
                entry['result'] = 'not_prime'
                entry['factors'] = factors
            elif number == 0:
                print(f"❌ 0 is NOT a prime number.")
                print("Factors: undefined\n")
                entry['result'] = 'not_prime'
                entry['factors'] = []
            elif number < 0:
                factors = get_factors(number)
                print(f"❌ {number} is NOT a prime number (negative integers are not prime).")
                print(f"Factors: {factors}\n")
                entry['result'] = 'not_prime'
                entry['factors'] = factors
            else:
                if is_prime(number):
                    print(f"✨ {number} is a PRIME number.\n")
                    entry['result'] = 'prime'
                    entry['factors'] = []
                else:
                    factors = get_factors(number)
                    print(f"❌ {number} is NOT a prime number.")
                    print(f"Factors: {factors}\n")
                    entry['result'] = 'not_prime'
                    entry['factors'] = factors
        elif kind == 'invalid_decimal':
            print(f"⚠️ Invalid input: '{user_input}' is a non-integer decimal. Please enter an integer.\n")
            entry['value'] = user_input
            entry['result'] = 'invalid_decimal'
        else:
            print(f"⚠️ Invalid input: '{user_input}'. Please enter an integer or 'End'.\n")
            entry['value'] = user_input
            entry['result'] = 'invalid'

        history.append(entry)

if __name__ == "__main__":
    main()