from stats import count_words
from stats import count_chars

#accept a filepath and return the contents of that file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#print the contents of the "get_book_text" file to the console
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_contents)
    characters = count_chars(book_contents)
    print (f"{word_count} words found in the document")
    print (characters)

main()