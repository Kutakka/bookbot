def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(get_book_text("/home/kutaka/projects/github.com/bookbot/books/frankenstein.txt"))

main()