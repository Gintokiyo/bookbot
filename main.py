def main():
    book_path = "books/frankenstein.txt"
    
    book_contents = get_book_text(book_path)
        
    word_count = count_words(book_contents)

    character_count = get_character_count(book_contents)

    data = char_dict_to_list(character_count)

    print_book_data(book_path, word_count, data)


def count_words(text : str):
    return len(text.split())


def get_book_text(path: str):
    with open(path) as f:
        return f.read()
    

def get_character_count(text: str):
    lower_text = text.lower()
    character_dict = {}
    for c in lower_text:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    return character_dict


def sort_on(dict: dict):
    return dict["count"]


def char_dict_to_list(dictionary: dict):
    dictionary_list = []
    for entry in dictionary:
        if entry.isalpha():
            dictionary_list.append({"name": entry, "count": dictionary[entry]})

    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

def print_book_data(path, word_count, dict_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document.")
    for dict in dict_list:
        print(f"The {dict['name']} character was found {dict['count']} times!")
    print("--- End report ---")


if __name__ == "__main__":
    main()