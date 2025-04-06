from stats import get_book_text, letter_counter, letter_sorter
import sys
import os

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

filepath = sys.argv[1]
word_count = get_book_text(filepath)
letter_list = letter_sorter(letter_counter(filepath))

if not os.path.isfile(filepath):
     print(f"Error: The file '{filepath}' does not exist or is not accessable")
     sys.exit(1)



def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in letter_list:
        char = item["letter"]
        count = item["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()