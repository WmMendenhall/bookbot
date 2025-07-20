#Split a string array into a list, then count the elements in the list.    
def count_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return (num_words)

def count_chars(text):
    unique_chars = {}
    lowercase = text.lower()
    for c in lowercase:
        if c in unique_chars:
            unique_chars[c] += 1
        else:
            unique_chars[c] = 1
    return (unique_chars)