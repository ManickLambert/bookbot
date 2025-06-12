def words_count(book_text):
    splited_text = book_text.split()
    num_words = len(splited_text)
    return num_words

def letter_count(book_text):
    text_lower = book_text.lower()
    letter_counts = {}
    for letter in text_lower:
        if letter.isspace():
            continue  # Skip all whitespace characters, not just spaces
        elif letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def sort_on(dict):
    return dict["num"]

def character_sort(dict):
    two_key_list = []
    for letter in dict:
        two_key_list.append({"char": letter, "num": dict[letter]})
    
    two_key_list.sort(reverse=True, key=sort_on)
    return two_key_list

