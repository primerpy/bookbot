def count_words(bookcontent: str) -> int:
    words_list = bookcontent.split()
    return len(words_list)


def count_letters(bookcontent: str) -> dict:
    res = {}
    for c in bookcontent:
        c = c.lower()
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


def sort_dict(bookdict: dict) -> list[dict]:
    book_dict_list = [
        {"char": k, "num": v} for (k, v) in bookdict.items() if k.isalpha()
    ]
    sorted_book_dict_list = sorted(book_dict_list, key=lambda x: x["num"], reverse=True)
    return sorted_book_dict_list
