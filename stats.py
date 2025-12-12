import sys
def main():
        # Check if user gave exactly one argument (the script name + book path)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_count = get_num_words(text)

    print("--------- Character Count -------")
    letter_counts = count_letters(text)
    print_letter_counts(letter_counts)

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    count = len(words)
    print(f"Found {count} total words")
    return count


def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


def print_letter_counts(letter_counts):
    # Sort by frequency (descending)
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # Print each letter like: a: 12345
    for letter, count in sorted_counts:
        print(f"{letter}: {count}")


main()
