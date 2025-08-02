import sys
from stats import count_words, count_letters, sort_dict


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    res = get_book_text(sys.argv[1])
    word_count = count_words(res)
    letter_count = count_letters(res)
    print(
        f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
"""
    )
    print(f"Found {word_count} total words")
    print(
        """
--------- Character Count -------
"""
    )
    sorted_letter_count = sort_dict(letter_count)

    for ele in sorted_letter_count:
        print(f"{ele['char']}: {ele['num']}")

    print(
        """
============= END ===============
"""
    )


if __name__ == "__main__":
    main()
