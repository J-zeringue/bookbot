def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_appearances = get_letter_count(text)
    letter_keys = list(letter_appearances.keys())
    char_letters = []

    print(text)

    for letter in letter_keys:
        if letter.isalpha():
            char_letters.append(letter)
    char_letters.sort()

    print(f"Begin report of {book_path}")
    print(f"{get_word_count(text)} words found in the document")
    for char in char_letters:
        print(f"The {char} was found {letter_appearances[char]}")


def get_letter_count(letter_count):
    letters_count = {}
    counter = 0
    for char in letter_count:
        lower_case = char.lower()
        if lower_case in letters_count:
            letters_count[lower_case] += 1
        else:
            letters_count[lower_case] = 1
    return letters_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(words):
    num_words = words.split()
    return len(num_words)


main()