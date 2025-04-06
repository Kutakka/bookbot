def get_book_text(filepath):
    file_contents = read_book(filepath)
    total_words = file_contents.split()
    num_words = len(total_words)
    return num_words

def letter_counter(filepath):
    counted_letters = {}
    file_contents = read_book(filepath)
    lowered = file_contents.lower()
    for letter in lowered:
        if letter not in counted_letters:
            counted_letters[letter] = 1
        else:
            counted_letters[letter] += 1
    return counted_letters

def letter_sorter(letter_dict):
    sorted_list = []
    for letter, count in letter_dict.items():
        if letter.isalpha():
            sorted_list.append({"letter": letter, "count": count})
    def sorter(item):
        return item["count"]
    sorted_list.sort(reverse=True, key=sorter)
    return sorted_list

def read_book(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

