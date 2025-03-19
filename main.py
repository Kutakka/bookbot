def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        total_words = file_contents.split()
        num_words = len(total_words)
        return num_words

def main():
    word_count = get_book_text("/home/kutaka/projects/github.com/bookbot/books/frankenstein.txt")
    print(f"{word_count} words found in the document")

main()