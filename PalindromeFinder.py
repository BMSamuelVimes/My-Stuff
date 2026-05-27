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
    all_are_palindromes = all(is_palindrome(word) for word in words_list)
    
    # 3. Display the final result
    print(f"\nYour words (Enter 'done' to end list): {words_list}")
    print(f"Result: {all_are_palindromes}")
    
    return all_are_palindromes

# Run the function
check_user_words()