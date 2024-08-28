def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(f"It contains {count_words(text)} words")
    print(count_chars(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    low_text = text.lower()
    char_count = {}
    for char in low_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


if __name__ == '__main__':
    main()

