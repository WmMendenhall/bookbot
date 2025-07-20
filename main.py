import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_words
from stats import count_chars
from stats import format_chars

#accept a filepath and return the contents of that file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#print the contents of the "get_book_text" file to the console
def main():
    book_contents = get_book_text(sys.argv[1])
    word_count = count_words(book_contents)
    characters = count_chars(book_contents)
    char_list = format_chars(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in char_list:
        if entry['char'].isalpha():
            print (f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()