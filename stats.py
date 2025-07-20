#Split a string array into a list, then count the elements in the list.    
def count_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return (num_words)


#Convert strings into lower case and returns the number of times each character, (including symbols and spaces), appears in the string.
def count_chars(text):
    unique_chars = {}
    lowercase = text.lower()
    for c in lowercase:
        if c in unique_chars:
            unique_chars[c] += 1
        else:
            unique_chars[c] = 1
    return (unique_chars)

#takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
def format_chars(characters):
    new_list = []
    for c in characters:
        count = characters[c]
        new_list.append({"char": c, "num": count})
    new_list.sort(reverse=True, key=lambda item: item["num"])
    return (new_list)