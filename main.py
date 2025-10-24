from stats import *
import sys
def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents=get_book_text(sys.argv[1])
    num_words=count_words(contents)
    chars_count=count_chars(contents)
    sorted_dict=sort_dict(chars_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for i in sorted_dict:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")
main()

