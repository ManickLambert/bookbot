from stats import words_count, letter_count, character_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():

    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    text = get_book_text(f"{sys.argv[1]}")
    print("----------- Word Count ----------")
    words = words_count(text)
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    letter = letter_count(text)
    two_key_dict = character_sort(letter)
    for i in two_key_dict:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
