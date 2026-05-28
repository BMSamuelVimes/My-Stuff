def is_palindrome(word):
    # Normalize the word to lowercase so capitalization doesn't break the check
    cleaned_word = word.lower()
    # Check if the word reads the same forwards and backwards
    return cleaned_word == cleaned_word[::-1]

def check_user_words():
    print("Enter your words one by one.")
    print("Type 'done' when you are finished entering words.\n")
    
    words_list = []
    
    # 1. Collect words from the user
    while True:
        user_input = input("Enter a word: ").strip()
        
        if user_input.lower() == 'done':
            break
        
        if user_input:  # Ensure the user didn't just press enter
            words_list.append(user_input)
            
    # Handle the edge case where the user enters no words at all
    if not words_list:
        print("\nNo words were entered.")
        return False

    # 2. Check if ALL words in the list are palindromes
    # The all() function returns True if all elements in the iterable are True
    palindromes = [w for w in words_list if is_palindrome(w)]
    not_palindromes = [w for w in words_list if not is_palindrome(w)]
    all_are_palindromes = all(is_palindrome(word) for word in words_list)

    yes_no = "YES" if all_are_palindromes else "NO"

    combined_no_space = " ".join(words_list).lower()
    combined_with_space = " ".join(words_list).lower()

    combined_no_space_is_pal = combined_no_space == combined_no_space[::-1]
    combined_with_space_is_pal = combined_with_space == combined_with_space[::-1]
    
    # 3. Display the final result
    print(f"\nYour words ({len(words_list)}): {words_list}")
    print(f"Are ALL entered palindromes? {yes_no}")
    if palindromes:
        print(f"Palindrome(s) ({len(palindromes)}): {palindromes}")
    if not_palindromes:
        print(f"Not Palindrome(s) ({len(not_palindromes)}): {not_palindromes}")
    if all_are_palindromes:
        combined_with_space_display = " ".join(palindromes)
        combined_no_space_display = "".join(palindromes)
        print(f"Combined (Space): {combined_with_space_display}")
        print(f"Combined (No Space): {combined_no_space_display}")
    
    print(f"Combined without spaces is a palindrome? {'Yes' if combined_no_space_is_pal else 'No'}")
    print(f"Combined with spaces is a palindrome? {'Yes' if combined_with_space_is_pal else 'No'}")
    
    return all_are_palindromes

# Run the function
check_user_words()