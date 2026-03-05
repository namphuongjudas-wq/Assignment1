def remove_odds(numbers):
    """
    Returns a new list containing only the even numbers from the input list.
    """
    # Using list comprehension for a concise, 'Pythonic' way to filter
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def main():
    # 1. Create a list of integers
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22]
    
    # 2. Call the function
    filtered_list = remove_odds(original_list)
    
    # 3. Print out both lists to compare
    print(f"Original List: {original_list}")
    print(f"Cut-down List: {filtered_list}")

# Run the main program
if __name__ == "__main__":
    main()