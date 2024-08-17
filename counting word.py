# Function to count the number of words in a given text
def count_words(text):
    # Strip leading/trailing whitespace and split the text into words
    words = text.strip().split()
    # Return the number of words
    return len(words)

# Main function to handle user input and control the program's logic
def main():
    # Take user input
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Basic control flow to check if the input is empty
    if user_input:
        # Call the count_words function to get the word count
        word_count = count_words(user_input)
        # Display the word count as output
        print(f"The number of words in the given text is: {word_count}")
    else:
        # Handle empty input by prompting the user again
        print("You didn't enter any text. Please try again.")
        main()  # Recursively call main() to ask for input again

# Entry point of the program
if __name__ == "__main__":
    main()
