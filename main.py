def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
#    print(text)
#    print(f"It contains {count_words(text)} words")
#    print(count_chars(text))
    report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def report(text):
    total_chars = count_words(text)
    char_count = count_chars(text)
    print(5*" === ")
    print(f"Report for Frankenstein book.")
    print(5 * " === ")
    print(f"Total words in the book is {total_chars}")
    print()
    print(f"Number of characters occurrence as follows - sorted by number of appearances:")
    for d in sorted(char_count, reverse=True, key=char_count.get):

        print(f"Character '{d}' - {char_count[d]} times")


def count_chars(text):
    low_text = text.lower()
    char_count = {}
    for char in low_text:
        if char not in char_count and char.isalpha():
            char_count[char] = 1
        elif char.isalpha():
            char_count[char] += 1
    return char_count


if __name__ == '__main__':
    main()

